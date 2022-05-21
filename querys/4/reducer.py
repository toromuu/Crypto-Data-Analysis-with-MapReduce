#!/usr/bin/python

# Dime de entre todas las monedas cual ha tenido el volumen de transacciones promedio más grande en la ultima semana.

import sys
from datetime import datetime, timedelta

volume  = 0
localMeanVolume = 0
maxVolume = 0
auxDate = 0
i=0
oldKey = None
cryptoMax = None

one_week_ago = datetime.today() - timedelta(days=7)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 4:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVolumefrom, thisVolumeto, thisDate = data_mapped

    if oldKey and oldKey != thisKey:
        localMeanVolume = localMeanVolume / i
        if localMeanVolume > maxVolume:
            maxVolume=localMeanVolume
            cryptoMax=oldKey
        oldKey = thisKey
        localMeanVolume = 0
        i = 0

    oldKey = thisKey

    auxDate = datetime.fromtimestamp(float(thisDate))
    if auxDate > one_week_ago:
        localMeanVolume += (float(thisVolumefrom) + float(thisVolumeto) ) / 2
        i += 1
            

if oldKey != None:
   print("%s\t%s" % (cryptoMax, maxVolume))