#!/usr/bin/python3
import csv
import sys

def titleFreq(data):
    dictTitles = {}
    for row in data[1:]:
        title = row[2]
        if title in dictTitles:
            dictTitles[title] += 1
        else:
            dictTitles[title] = 1
    return dictTitles.items()

def degreeFreq(data):
    dictDegrees = {}
    for row in data[1:]:
        degree = row[1]
        if degree in dictDegrees:
            dictDegrees[degree] += 1
        else:
            dictDegrees[degree] = 1
    return dictDegrees.items()

def emailList(data):
    emails = []
    for row in data[1:]:
        emails += [row[3]]
    return emails

facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

print(titleFreq(facultyData))
print(degreeFreq(facultyData))

print(facultyData[0])
print(emailList(facultyData))
