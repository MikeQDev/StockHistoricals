#!/usr/bin/python
import csv
import sys
import urllib

if len(sys.argv) != 2:
  print "usage: python "+sys.argv[0]+" analyzed-ratio-sorted.csv"
  exit()


#count lines, so we know the last ones to pull..
amount = 0
with open(sys.argv[1],'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    amount += 1
 

_BASE_URL_ = "https://www.google.com/finance/getchart?x=NASD&p=40Y&i=604800&ei=J092WJCaO4HRjAH27rbYBA&q="
i = 0;
with open(sys.argv[1],'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    i = i+1
    if i == 1:
      continue
    elif i > 50 and i < (amount-50):
      continue

    print "status: grabbing "+str(i)
    ticker = row[0][1:-1]
    ratio = row[1] 
    urllib.urlretrieve(_BASE_URL_+ticker, "graphs/"+ratio+"-"+ticker+".png")
