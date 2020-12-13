# securityProject
WebVulnerabilitiesScanner

<h1>Foreword</h1>
The purpose of this scanner is to help you analysing you website in order to show the different problems regarding the security of it, and to correct it.
We are using different tools like Nikto, Wapiti, dirsearch to scan the files and configurations of your web application.
We are not responsible of the actions you are doing with this script and encourage you to only scan your websites.

<h1>Requirements</h1>
This script uses differents other script to work.
We recommand you to use Kali Linux to lauch it, beacause tools used like Nikto, Wapiti and Python3 are already installed.
If you are uysing an other Linux distribution, you may dowload and install these tools.

<h1>Usage</h1>
Once you have download the scanner, you may go in its directory and open a shell.
Type this command to run the bottle webserver : "python3 app.py".
You can now access the scanner directly from a browser with : http://localhost:8080
Differents options are available for a scan:

<h2>-1 For Dirsearch</h2>, you shoul specify a wordlist to crawl the tested website, the bigger the wordlist is the longer the scan well be. If you want to modify a wordlist, go into the root folder and add some stuff in filsNdirs.wordlist (the medium option in the scanner).

<h2>-2 For Nikto</h2>, the same pattern is designed. The option lite/full scan depend of the time and how deep you want to pass in the scan.
Check Enable SSL for https websites or Disable for http websites.
The last options allow you to add a timeout.

<h2>-3 The Wapiti's options</h2> will ask you to check the vulnerabilities you want to test.
For more informations about the tools used, please refer to the link on the scanner page.

Finnaly, input the url of the website to test in the input part.
The format should be :"http(s)://'ip'/'domain'.'com/fr':'port'"
