from bottle import Bottle, run, static_file, template, request #Allow to use Bottle functions
import os, sys, webbrowser
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

    if not testedURL:
        return "Veuillez entrer une URL"

    result = subprocess.run(['sudo', '../dirsearch/dirsearch.py', '-u', testedURL, '-e', 'php,html,txt', '-w', #Scanning with Dirsearch, using a
     ROOT_PATH + usedWordlist, '--simple-report', 'results/target.txt'])                                       #wordlist choosen by the suer and create a simple ouput
                                                                                                               #in results/target.txt

    with open('results/target.txt', 'r') as readFile:
        with open('views/scanner.html','w') as writeFile:
            writeFile.write("%rebase('base.tpl')\n")
            for line in readFile:
                writeFile.write(line)
                writeFile.write('</br>')
            writeFile.write(" </body> \n</html")

    filename = 'http://localhost:8080/scanner'
    webbrowser.open(filename)

    niktoResults = subprocess.run(['sudo', 'nikto', '-host', testedURL, '-output', ROOT_PATH + '/results/niktoResult.txt', '-Tuning', tV1, tV2, '-maxtime', tV5, tV6, '-ask', 'no', tV3, tV4])

    with open('results/niktoResult.txt', 'r') as readFile:
        with open('views/vuln1.html','w') as writeFile:
            writeFile.write("%rebase('base.tpl')\n")
            for line in readFile:
                writeFile.write(line)
                writeFile.write('</br>')
            writeFile.write(" </body> \n</html")

    filename = 'http://localhost:8080/vuln1'
    webbrowser.open(filename)
    #
    wapitiResult = subprocess.run(['sudo', 'wapiti', '-u', testedURL, '-o', ROOT_PATH + '/results/wapitiResult.txt', '-f', 'txt', '-v', '1'])

    with open('results/wapitiResult.txt', 'r') as readFile:
        with open('views/vuln2.html','w') as writeFile:
            writeFile.write("%rebase('base.tpl')\n")
            for line in readFile:
                writeFile.write(line)
                writeFile.write('</br>')
            writeFile.write(" </body> \n</html")

    filename = 'http://localhost:8080/vuln2'
    webbrowser.open(filename)


#Pour passer les arguments à une autre commande : result2 = subprocess(['grep', '-n', 'index.html'], capture_output=True, text=true, input=result.output)


run(app, host='localhost', reloader=True, debug=True, port=8080)
