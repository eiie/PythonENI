import csv

port = "80"

with open("dictionaries/service-names-port-numbers.csv","r") as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if row[2] == "tcp":
                if row[1] == port:
                    print row[0], row[1], row[2]
