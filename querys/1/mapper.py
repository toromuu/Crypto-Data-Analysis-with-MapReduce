#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 10:
        time, high, low, open, volumefrom, volumeto, close, conversionType, conversionSymbol, name = data
        print("{0}\t{1}\t{2}".format(name, open, close ))
