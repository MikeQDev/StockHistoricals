#!/usr/bin/python
import csv
import sys

if len(sys.argv) != 2:
  print "usage: python "+sys.argv[0]+" inCompanyListFile.csv"
  exit()
else:
  print sys.argv[1]


with open(sys.argv[1],'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print row[0]
