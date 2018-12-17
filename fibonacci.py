def suiteFibonacci(nbF):
    i = 0
    j = 1
    a = 1
    if nbF == 0 :
        tmp = 0
    elif nbF == 1 :
        tmp = 1
    else :
       while a < nbF :
            tmp = i + j
            i = j
            j = tmp
            a += 1
        #print tmp
    print "F" + str(nbF) + " = " + str(tmp)

while True :
    try :
        nbF = int(raw_input("Entrer un nombre de Fibonacci : "))
        break
    except ValueError :
        print "Saisie invalide !"

suiteFibonacci(nbF)
