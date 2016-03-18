# The football.csv file contains results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and has 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

import csv
import sys

footballFile = open('football.csv')
footballReader = csv.reader(footballFile)
footballData = list(footballReader)

dif = sys.maxint
mindifteam = ''

for row in footballData[1:]:
    teamdif = abs(int(row[5])-int(row[6]))
    if teamdif < dif:
        dif = teamdif
        mindifteam = row[0]

print mindifteam
