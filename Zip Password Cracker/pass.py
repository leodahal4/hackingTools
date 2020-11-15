#
# You can run this file as
# python3 pass.py -w wordlist_path -z zipfile.zip
# Written By
#   - Leo Dahal
#



import optparse
import zipfile
from tqdm import tqdm

class Crack():
    def __init__(self, wordList, zipFileName):
        # takes two argument i.e wordlist file path and the zip-file name to
        # brute-force on
        self.wordList = wordList
        self.zipFileName = zipFileName

        self.zipFileObject = zipfile.ZipFile(self.zipFileName)
        self.words = len(list(open(self.wordList, "rb")))
        print("Total password to brute-force:\t", self.words)
        self.crack()

    def crack(self):
        with open(self.wordList, "rb") as wordList:
            for self.word in tqdm(wordList, total=self.words, unit="word"):
                try:
                    self.zipFileObject.extractall(pwd=self.word.strip())
                except:
                    continue
                else:
                    print("\n[+] Password found:", self.word.decode().strip())
                    exit(0)
        print("\n[!] Password not found, try other wordlist.")

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--wordlist", dest="wordlist", help="List of passwords to try")
    parser.add_option("-z", "--zipfile", dest="zipFileName", help="Zip file to brute-force on")
    (options, arguments) = parser.parse_args()
    return options.wordlist, options.zipFileName

wordList, zipFileName = getArguments()

process = Crack(wordList, zipFileName)

