# Simple program to read CSV files
# Write a program to read in the data and output each line as a list
# Author: Francesca Ruberto

import csv

FILENAME = "data.csv"
DATADIR = "../mywork/"

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    for line in reader:
        print(line)


# Modify the program to deal with the header line separately

FILENAME = "data.csv"
DATADIR = "../mywork/"

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    linecount = 0 
    for line in reader:
        if not linecount:
            print (f"{line}\n------------------")
    else:
        print (line)
    linecount +=1

# Modify the program to calculate the average age, there are a few ways to solve this;

