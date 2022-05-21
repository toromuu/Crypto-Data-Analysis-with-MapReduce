#!/usr/bin/python

# Dime las monedas cuya diferencia más grande entre open y close sea mayor a un 50% en el ultimo año

import sys
from datetime import datetime, timedelta

auxDate = 0
oldKey = None
lastYear = datetime.today() - timedelta(days=365)

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

    if auxDate > lastYear and 0.5*float(thisOpen) < diff:
        print("%s\t%s\t%s" % (oldKey, diff, auxDate))

if oldKey != None:
   print("%s\t%s\t%s" % (oldKey, diff, auxDate))