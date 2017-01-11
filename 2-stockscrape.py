#!/usr/bin/python
import requests # for making requests to yahoo finance
import csv      # for parsing CSV data from yahoo finance
import json
import sys

if len(sys.argv) != 2:
  print "usage: python "+sys.argv[0]+" inCompanyListFile.csv"
  exit()

URL = "http://chart.finance.yahoo.com/table.csv?a=10&b=23&c=2010&d=10&e=23&f=2016&g=m&ignore=.csv"
STOCK_LIST = ['CAPR','A','QQQ','T','GCO','UTX','CI']#,'B','C']
for line in open(sys.argv[1],'r').readlines():
  STOCK_LIST.append(line[:-1])
print 'Loaded '+str(len(STOCK_LIST))+" symbols!"
# open file
#print(STOCK_LIST)
myFile = open('something','w+')
index = 0
print 'curPrice,lowest'
# csv columns: date (0), open (1), high (2), low (3), close (4), volume (5), adj close (6)
for ticker in STOCK_LIST:
  # print 'trying: '+ticker
  index = index + 1
  # get historical data
  histData = csv.reader(requests.get(URL+"&s="+ticker).iter_lines())#,delimiter=',')
  histLowest = 9999
  rowNum = 0
  for row in histData:
    rowNum = rowNum + 1
    if rowNum == 1: # first row: skip headers
      continue         
    try:
      low = float(row[3])
    except:
      print "lol"
      #print "Issue getting price for "+ticker+"! Continuing onto next..."
    if low < histLowest:
      histLowest = low

  # get current price
  data = requests.get('https://www.google.com/finance/getprices?q='+ticker+'&i=120&p=25m&f=d,c,v,o,h,l&df=cpct&auto=1').content
  split = str(data).splitlines()
  curPrice = -1
  for line in split:
    if line[:2] == '1,':
      curPrice = line.split(',')[2]
  if curPrice == -1:
      continue;
  outStr = str(index)+":["+ticker+"]\t"+str(curPrice)+","+str(histLowest)
  print outStr
  myFile.write(outStr+'\n')
myFile.close()
