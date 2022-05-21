#!/usr/bin/python

import sys
from datetime import datetime, timedelta

auxDate = 0
oldKey = None
halfmonth = datetime.today() - timedelta(days=15)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 4:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisOpen, thisClose, thisDate = data_mapped

    if oldKey and oldKey != thisKey:
        oldKey = thisKey
        diff = 0

    oldKey = thisKey
    diff= abs(float(thisOpen) - float(thisClose) ) 
    auxDate = datetime.fromtimestamp(float(thisDate))

    if auxDate > halfmonth and 0.5*float(thisOpen) < diff:
        print("%s\t%s\t%s" % (oldKey, diff, auxDate))

if oldKey != None:
   print("%s\t%s\t%s" % (oldKey, diff, auxDate))