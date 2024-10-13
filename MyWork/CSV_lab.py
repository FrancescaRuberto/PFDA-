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

# First method - convert the str into an int
FILENAME = "data.csv"
DATADIR = "../mywork/"

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    linecount = 0 #used to count number of raws red
    total = 0 # used to sum the valus of a column (age in my case)
    for line in reader:
        if not linecount:
            pass # meaning to skip the first raw in the reader
        else: # means we sum all the number in the second column for each row
            total += int(line[1]) #we put 1 because we want to start from the second column of each row, if the first is 0
        linecount += 1 # we increase the counter of 1 each time e row is red
    print (f"average is {total/(linecount-1)}") # we put -1 bacause we want to not include first row 

# Second method - use the quote parameter to read in the numbers as floats

FILENAME = "data.csv"
DATADIR = "../mywork/"

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0 #used to count number of raws red
    total = 0 # used to sum the valus of a column (age in my case)
    for line in reader:
        if not linecount:
            pass
        else:
            total += 1 # we increase the counter of 1 each time e row is red
        linecount += 1 # we increase the counter of 1 each time e row is red
    print (f"average is {total/(linecount-1)}") # we put -1 bacause we want to not include first row 

# We can also read the CSV file as Dictionary object by using DictReader()

FILENAME = "data.csv"
DATADIR = "../mywork/"

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.DictReader(fp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0 # count how many rows with data are red
    for line in reader:
        total += line['age']
        # print (line)
        count += 1 # increase counter for each row red, in order to calculate average at the end
    print (f"average is {total/(count)}") # here I do not need for the header to be eliminated from count since DictReader alseady do this for me 


