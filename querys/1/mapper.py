#!/usr/bin/python

# ACTIVIDAD 4
# Obtener la suma total de ventas para cada categoría de
# producto, independientemente de la tienda en la que se haya realizado la compra

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 10:
        time, high, low, open, volumefrom, volumeto, close, conversionType, conversionSymbol, name = data
        #print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(time, high, low, open, volumefrom, volumeto, close, conversionType, conversionSymbol, name))
        print("{0}\t{1}\t{2}".format(name, open, close ))


