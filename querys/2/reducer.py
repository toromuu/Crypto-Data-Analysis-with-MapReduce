#!/usr/bin/python


# Para cada moneda dime la fecha donde tuvo su valor más alto

import sys
import datetime

value  = 0
date = 0
max = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 4:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisOpen, thisClose, thisDate = data_mapped

    if oldKey and oldKey != thisKey:
        print("%s\t%s\t%s" % (oldKey, max, int(datetime.date.fromtimestamp(date))))
        oldKey = thisKey
        value  = 0
        max = 0
        date = 0

    oldKey = thisKey
    value  = (float(thisOpen) + float(thisClose) ) / 2

    if max < value:
        max = value
        date = int(thisDate)

if oldKey != None:
   print("%s\t%s\t%s" % (oldKey, max, int(datetime.date.fromtimestamp(date))))