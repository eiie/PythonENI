f = open("yo.slp","r")
lines = f.readlines()
stop = False
for line in lines :
    if stop == True:
        print line
        break
    elif line == "a\n":
        stop = True
    else:
        continue
