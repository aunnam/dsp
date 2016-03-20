#!/usr/bin/python3
import csv
import sys

def titleDict(data):
    dictTitles = {}
    for row in data[1:]:
        title = row[2]
        if title in dictTitles:
            dictTitles[title] += 1
        else:
            dictTitles[title] = 1
    return dictTitles

def degreeDict(data):
    dictDegrees = {}
    for row in data[1:]:
        degree = row[1].split(' ')
        for x in range(len(degree)):            
            if degree[x] != '':
                if degree[x] in dictDegrees:
                    dictDegrees[degree[x]] += 1
                else:
                    dictDegrees[degree[x]] = 1
    return dictDegrees

def emailList(data):
    emails = []
    for row in data[1:]:
        emails += [row[3]]
    return emails

def domainDict(data):
    emails = emailList(data)
    dictDomain = {}
    for email in emails:
        user, domain = email.split('@')
        if domain in dictDomain:
            dictDomain[domain] += 1
        else:
            dictDomain[domain] = 1
    return dictDomain

facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

# print(titleDict(facultyData).items())
# print(degreeDict(facultyData).items())

domainDictionary = domainDict(facultyData)

print(domainDictionary.items())

for k,v in domainDictionary.items():
    if v == 1:
        print(k+ " is a unique email domain")

print(facultyData[0])
# print(emailList(facultyData))
