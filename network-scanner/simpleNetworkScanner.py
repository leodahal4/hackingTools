import subprocess
import optparse
try:
    import scapy.all as scapy

except:
    print("Provide password for installing scapy.")
    subprocess.call("sudo pip3 install scapy", shell=1)




class Network():
    def __init__(self, ip):
        self.ip = ip
        self.scan()

    def scan(self):
        arpRequest = scapy.ARP(pdst=self.ip)
        bordcastMac = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

        try:
            connectedClients = scapy.srp(bordcastMac/arpRequest, timeout=1, verbose=0)[0]
            self.connectedNodes = []
            for nodes in connectedClients:
                self.connectedNodes.append({"IP": nodes[1].psrc, "MAC": nodes[1].hwsrc})
        except:
            subprocess.call("clear", shell=1)
            print("Please provide sudo permission for scanning the network.")
            exit(0)

        self.printOut()

    def printOut(self):
        self.clearScreen()
        self.totalClients()
        print(f"There are total {self.totalNodes} devices connected to this network.")
        print("\t_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        print("\tIP\t\t\t MAC")
        print("\t--------------------------------------------\n")
        for nodes in self.connectedNodes:
            print("\t" + nodes["IP"]+ "\t|\t" + nodes["MAC"])

    def totalClients(self):
        self.totalNodes = 0
        for nodes in self.connectedNodes:
            self.totalNodes += 1

    def clearScreen(self):
        for i in range(1,100):
            print("")


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


print("Scanning...")
options = getArguments()
checkArguments(options)
scanthis = Network(options.target)
