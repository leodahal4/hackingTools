#!/usr/bin python

# SIMPLE HTTP HEADER CHECKER
# description:  http header vulnerability analysis project
# github: https://github.com/leodahal4/hackingTools/vulnchecker
# version: 1

import urllib3
import optparse
import subprocess

def checkArguments(options):
    if (options.target == None):
        subprocess.call("clear", shell=True)
        print("Please provide IP or IP range.\nTry running with --help options.")
        exit(0)

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target Ip / Tagrget Ip/Range")
    (options, arguments) = parser.parse_args()
    return options


class Scan():
    def __init__(self, target):
        self.target = target
        self.start()

    def start(self):
        http = urllib3.PoolManager()
        self.response = http.request("GET", "https://" + options.target)
        self.checkVulnerability()

    def checkVulnerability(self):
        self.printResult()

    def printResult(self):
        print(self.response.headers)


print("Scanning...")
options = getArguments()
checkArguments(options)
Scan(options.target)




