# CSV module practice

#Simple program to read a CSV file

import csv

FILENAME= "data.csv"
DATADIR = "../Others/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            print (f"{line}\n-------------")
        else: 
            total += int(line[0])
            print (line)
        linecount += 1
