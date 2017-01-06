#!/usr/bin/python
print "\tcur:low ratio\tcurPrice\tlow\tdiff"
with open('something') as infile:
   for line in infile:
     split = line.split('\t')[1].split(',')
     cur = split[0]
     low = split[1]
     if cur == '-1':
       continue
     ratio = float(cur)/float(low)
     diff = float(cur) - float(low)
     print line.split('\t')[0].split(':')[1]+"\t"+str(ratio)+"\t"+str(cur)+"\t"+str(low).strip()+"\t"+str(diff)
     #print cur + "," + low
