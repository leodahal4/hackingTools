#!/usr/bin python

# HTTP HEADER CHECKER
# description:  http header vulnerability analysis project
# github: https://github.com/leodahal4/hackingTools/vulnchecker
# version: 0.1

import urllib3
import optparse
import subprocess

class Scan():
    def __init__(self, target):
        self.target = target
        self.start()

    def start(self):
        try:
            http = urllib3.PoolManager()
            self.response = http.request("GET", "https://" + options.target)
            self.checkVulnerability()
        except:
            self.printResult(
                "Check your connectivity!"\
                "\nOr if not, make sure that the host is up.\n"
            )

    def checkVulnerability(self):
        #X-XSS-Protection
        if "x-xss-protection" not in self.response.headers:
            self.printResult("Vulnerable to Cross Site Scripting")
        else:
            pass

        # X-Frame-Options
        if "x-frame-options" not in self.response.headers:
            self.printResult("Vulnerable to Click jacking attack")
        else:
            pass

        #X-Content-Type-Options
        if "x-content-type-options" in self.response.headers:
            if self.response.headers["x-content-type-options"] == "nosniff":
                pass
            else:
                self.printResult("vulnerable to MIME-Scripting")
        else:
            self.printResult("vulnerable to MIME-Scripting")

        #strict-transport-security
        if "strict-transport-security" not in self.response.headers:
            self.printResult("vulnerable to MITM attack as the site can load without SSL")
        else:
            pass

        #content-security-policy
        if "content-security-policy" not in self.response.headers:
            self.printResult("Vulnerable to Cross-Site Scripting")
        else:
            pass

        #access-control-allow-origin
        if "access-control-allow-origin" not in self.response.headers:
            self.printResult("Vulnerable to Cross-Domain Scripting Attacks")
        else:
            pass

        #x-download-options
        if "x-download-options" in self.response.headers:
            if self.response.headers["x-download-options"] == "noopen":
               pass
            else:
                self.printResult("vulnerable to Browser File Execution Attacks")
        else:
            self.printResult("vulnerable to Browser File Execution Attacks")

        #x-permitted-cross-domain-policies
        if ("x-permitted-cross-domain-policies" in self.response.headers):
            if self.response.headers[
                "x-permitted-cross-domain-policies"
            ] == "master-only" or self.response.headers[
                "x-permitted-cross-domain-policies"
            ] == "none":
                pass
            else:
                self.printResult("Vulnerable to Cross-Protocol-Scripting Attacks")
        else:
            self.printResult("Vulnerable to Cross-Protocol-Scripting Attacks")

    def printResult(self, vul):
        print("" + vul)


def checkArguments(options):
    if (options.target == None):
        subprocess.call("clear", shell=True)
        print("Seriously ?\n\nTry running with --help options.")
        exit(0)

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target website")
    (options, arguments) = parser.parse_args()
    return options


subprocess.call('clear', shell=True)
print('HTTP header checker')
print('Github: https://github.com/leodahal4/hackingTools/vulnchecker\n')
print('Scanning...\n\n')
options = getArguments()
checkArguments(options)
Scan(options.target)
