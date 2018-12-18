from scapy.all import *

host = "10.101.200.28"
port = 80 

def scan_host_scapy(host, port):
    conf.verb = 0
    a = IP()
    b = TCP()
    a.dst = host
    b.sport = RandShort()
    b.dport = port
    b.flags = "S"
    
    res = sr1(a/b)
    res.show()

    flag = res.getlayer(TCP).flags

    if flag == "SA":
        return 0
    else:
        return 1

response = scan_host_scapy(host,port)

if response == 0:
    print "ouvert"
else:
    print "ferme"

