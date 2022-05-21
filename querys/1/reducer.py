#!/usr/bin/python

import sys

mean = 0
i = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisOpen, thisClose = data_mapped

    if oldKey and oldKey != thisKey:
        mean = mean / i
        print("%s\t%s" % (oldKey, mean))
        oldKey = thisKey
        mean = 0
        i=0

    oldKey = thisKey
    mean += (float(thisOpen) + float(thisClose) ) / 2
    i += 1

if oldKey != None:
    mean = mean / i
    print("%s\t%s" % (oldKey, mean))
