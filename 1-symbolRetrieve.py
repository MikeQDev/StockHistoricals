#!/usr/bin/python
import csv

with open('companylist.csv','rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print row[0]
