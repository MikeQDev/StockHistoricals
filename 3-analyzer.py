#!/usr/bin/python
import sys

if len(sys.argv) != 2:
  print "usage: python "+sys.argv[0]+" base-data.csv"
  exit()


print "\tcur:low ratio\tcurPrice\tlow\tdiff"

with open(sys.argv[1]) as infile:
   for line in infile:
     split = line.split('\t')[1].split(',')
     cur = split[0]
     low = split[1]
     if cur == '-1':
       continue
     ratio = float(cur)/float(low)
     diff = float(cur) - float(low)
     print line.split('\t')[0].split(':')[1]+","+str(ratio)+","+str(cur)+","+str(low).strip()+","+str(diff)
     #print cur + "," + low
