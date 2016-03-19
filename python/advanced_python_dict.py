#!/usr/bin/python3
import csv
import sys

facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

def q6Dict(data):
    dict1 = {}
    for row in data[1:]:
        name = row[0]
        splitName = name.split(' ')
        if len(splitName)==2:
            lastName = splitName[1]
        else: 
            lastName = splitName[2]
        if lastName in dict1:
            dict1[lastName] += [row[1:]]
        else:
            dict1[lastName] = [row[1:]]
    return dict1

def q7Dict(data):
    dict2 = {}
    for row in data[1:]:
        name = row[0]
        splitName = name.split(' ')
        if len(splitName)==2:
            lastName = splitName[1]
        else: 
            lastName = splitName[2]
        firstName = splitName[0]
        dict2[(firstName,lastName)] = row[1:]
    return dict2

def q8DictPrint(data):
    dict2 = q7Dict(data)
    sortedkeys = sorted(dict2, key=lambda key: key[1])
    count = 0
    for i in sortedkeys:
        if count == 3:
            break
        else:
            print(i,dict2[i])
            count += 1
    return

q6Dictionary = q6Dict(facultyData)
q7Dictionary = q7Dict(facultyData)

q8DictPrint(facultyData)


# count = 0
# for key,value in q6Dictionary:
#     if count == 3:
#         break
#     print(key, value)
#     count += 1
