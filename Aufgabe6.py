import csv

relation = {}
ifile  = open('relation.csv', "r")
read = csv.reader(ifile, delimiter = ";")
for row in read:
    if row[0] in relation:        
        relation[row[0]].append(row[1])
    else:
        relation[row[0]] = [row[1]]

print(len(relation))
print(relation["mccarty-d"])



def breadth(dicton, start):
    visited = []
    queue = []
    queue.append(start)
