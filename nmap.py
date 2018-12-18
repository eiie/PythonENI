from socket import *
import sys, time
from datetime import datetime
import os

host = ''
min_port = 78
max_port = 82

def scan_host(host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host, port))
        if code == 0:
            r_code = code
        s.close()
    except:
        pass
    return r_code

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
        try:
            response = scan_host(host, port)
            if response == 0:
                print "\t[+] Open Port : " + str(port) 
            else:
                print "\t[-] Closed Port : " + str(port)
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
