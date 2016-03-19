#!/usr/bin/python3
import csv
import sys

facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

def emailList(data):
    emails = []
    for row in data[1:]:
        emails += [row[3]]
    return emails

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow([line])

csv_writer(emailList(facultyData), 'emails.csv')

