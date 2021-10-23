import nmap
import optparse

def parser():

    parser = optparse.OptionParser('%prog [host]/[mask]')

    (options,args) = parser.parse_args()

    return args


def networkScanner(network):

    nm = nmap.PortScanner()
    print(nm.scan(hosts=network,arguments="-sn").hosts)
    

        

def main():

    netwrok = parser()[0]
    networkScanner(netwrok)


if __name__ == '__main__':

    main()