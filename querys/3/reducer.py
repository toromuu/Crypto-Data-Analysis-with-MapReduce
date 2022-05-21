#!/usr/bin/python

import sys
from datetime import datetime, timedelta

date = 0
auxDate = 0
max = 0
oldKey = None
thirty_days_ago = datetime.today() - timedelta(days=30)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisClose, thisDate = data_mapped

    if oldKey and oldKey != thisKey:
        print("%s\t%s\t%s" % (oldKey, max, date))
        oldKey = thisKey
        max = 0
        date = 0

    oldKey = thisKey
    auxDate = datetime.fromtimestamp(float(thisDate))

    if auxDate > thirty_days_ago and max < float(thisClose):
        max = float(thisClose)
        date = auxDate

if oldKey != None:
   print("%s\t%s\t%s" % (oldKey, max, date))