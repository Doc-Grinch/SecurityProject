from bottle import Bottle, run, static_file, template, request #Allow to use Bottle functions
import os, sys, webbrowser, re
from pprint import pprint                                   #Allow to interact with the system
import subprocess                                              #Allow to use system commands
from subprocess import PIPE

app = Bottle()

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))         #/home/USER/Documents/Projetc/Site
BOOTSTRAP_PATH = os.path.join(ROOT_PATH, "static")             #Feni the acces to yhe statics file like .css

@app.route('/static/<filepath:path>')
def bootstrap_static(filepath):
    return static_file(filepath, root=BOOTSTRAP_PATH)

@app.route('/')                                                #Defini the access to the index
@app.route('/index')
def showIndex():
    return template("views/index.html")

@app.route('/vuln1')
def showVuln1():
        return template("views/vuln1.html")

@app.route('/vuln2')
def showVuln1():
        return template("views/vuln2.html")

@app.route('/scanner', method='GET')                           #Define the acces to scanner.html and display the scan
def showScann():
    return template("views/scanner.html")

@app.route('/scan', method='POST')                             #Define crawler instructions, datas from the form and the output
def testURL():

    #URL
    testedURL = request.forms.testedURL
    #Wordlist to use
    usedWordlist = request.forms.usedWordlist
    #Nikto's options
    tV1 = request.forms.niktoOptions1
    tV2 = request.forms.niktoOptions2
    tV3 = request.forms.niktoOptions3
    tV4 = request.forms.niktoOptions4
    tV5 = request.forms.niktoOptions5
    tV6 = request.forms.niktoOptions6
    #Wapiti's Options
    wo1 = request.forms.wapitiOption1
    wo2 = request.forms.wapitiOption2
    wo3 = request.forms.wapitiOption3
    wo4 = request.forms.wapitiOption4
    wo5 = request.forms.wapitiOption5
    wo6 = request.forms.wapitiOption6
    wapitiAllOptions = wo1+','+wo2+','+wo3+','+wo4+','+wo5+','+wo6


    if not testedURL:
        return "Veuillez entrer une URL"

    result = subprocess.run(['sudo', '../dirsearch/dirsearch.py', '-u', testedURL, '-e', 'php,html,txt', '-w', #Scanning with Dirsearch, using a
     ROOT_PATH + usedWordlist, '--simple-report', 'results/target.txt'])                                       #wordlist choosen by the user and create a simple ouput
                                                                                                               #in results/target.txt

    with open('results/target.txt', 'r') as readFile:
        with open('views/scanner.html','w') as writeFile:
            writeFile.write("%rebase('baseScanner.tpl')\n")
            writeFile.write("<h2>Dirsearch's results</h2> \n")
            for line in readFile:
                writeFile.write(line)
                writeFile.write('  </br>')

    niktoResults = subprocess.run(['sudo', 'nikto', '-host', testedURL, '-Tuning', tV1, tV2, '-maxtime', tV5, tV6, '-ask', 'no', tV3, tV4, '-output', ROOT_PATH + '/results/niktoResult.txt'])

    with open('results/niktoResult.txt', 'r') as readFile:
        with open('views/scanner.html','a') as writeFile:
            writeFile.write("<h2>Nikto's results</h2> \n")
            for line in readFile:
                writeFile.write(line)
                writeFile.write('  </br>')

    wapitiResult = subprocess.run(['sudo', 'wapiti', '-u', testedURL, '--flush-session', '-o', ROOT_PATH + '/results/wapitiResult.txt', '-f', 'txt', '-v', '1','-m', wapitiAllOptions]) 

    with open('results/wapitiResult.txt', 'r') as readFile:
        with open('views/scanner.html','a') as writeFile:
            writeFile.write("<h2>Wapiti's results</h2> \n")
            for line in readFile:
                writeFile.write(line)
                writeFile.write('  </br>')
            writeFile.write("\n  </div> \n </body> \n</html>")

    os.remove("/home/bobby/ProjetSécu/securityProject/Site/results/niktoResult.txt")
    os.remove("/home/bobby/ProjetSécu/securityProject/Site/results/target.txt")
    os.remove("/home/bobby/ProjetSécu/securityProject/Site/results/wapitiResult.txt")

    return template("views/scanner.html")

# Pour passer les arguments à une autre commande : result2 = subprocess(['grep', '-n', 'index.html'], capture_output=True, text=true, input=result.output)


run(app, host='localhost', reloader=True, debug=True, port=8080)
