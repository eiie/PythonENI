from socket import *
import sys, time
from datetime import datetime
import os
from scapy.all import *
import csv

def scan_host(host, port):
    conf.verb = 0

    a = IP()
    b = TCP()
    a.dst = host
    b.sport = RandShort()
    b.dport = port
    b.flags = "S"
    
    res = sr1(a/b)

    flag = res.getlayer(TCP).flags

    if flag == "SA":
        return 0
    else:
        return 1

def main():
    try:
        os.system('cls')
        print "\n"
        print("""\
  _   _                 _     _        ____                                  
 | | | |_   _ _ __ ___ | |__ | | ___  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |_| | | | | '_ ` _ \| '_ \| |/ _ \ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 |  _  | |_| | | | | | | |_) | |  __/  ___) | (_| (_| | | | | | | |  __/ |   
 |_| |_|\__,_|_| |_| |_|_.__/|_|\___| |____/ \___\__,_|_| |_|_| |_|\___|_|  

         """)
        host = raw_input("\tEnter host IP address to scan: ")
        min_port = int(raw_input("\tEnter min port: "))
        max_port = int(raw_input("\tEnter max port: "))
    except KeyboardInterrupt:
        print "Interrupted by user"
        sys.exit(1)

    print "\n\t---"
    print "\tHost IP : " + host
    print "\tScanning Started At %s ... " % (time.strftime("%H:%M:%S"))
    print "\t---\n"
    start_time = datetime.now()

    for port in range(min_port, max_port):

        prot = ""

        with open("dictionaries/service-names-port-numbers.csv","r") as csvfile:
                reader = csv.reader(csvfile,delimiter=',')
                for row in reader:
                    if row[2] == "tcp":
                        if row[1] == str(port):
                            prot = prot + "\t" + row[0]

        try:
            response = scan_host(host, port)
            if response == 0:
                print "\t[+]\033[92m Open Port \033[00m  : " + str(port) + prot
            else:
                print "\t[-]\033[91m Closed Port\033[00m : " + str(port) + prot
        except KeyboardInterrupt:
            print "Interrupted by user"
            sys.exit(1)

    stop_time = datetime.now()
    total_time = stop_time - start_time
    print "\n\t---"
    print "\tScanning Finished At %s ..." % (time.strftime("%H:%M:%S"))
    print "\tScanning Duration: %s ..." % (total_time)
    print "\t---\n"

main()
