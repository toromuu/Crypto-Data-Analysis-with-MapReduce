import argparse
import matplotlib.pyplot as plt
import random
import numpy as np
from prettytable import PrettyTable

if __name__ == '__main__':

    labels = []
    values = []
    dates = []
    lab_val = []

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed with extension")
    parser.add_argument("filename_out", help="The filename result with extension")
    parser.add_argument("mode", help="Mode is required. Select between table or bar-plot")
    parser.add_argument("dateMode", help="Mode is required. Select between on or off")
    parser.add_argument("value_column", help="Value_column 2 is required")
    parser.add_argument("title", help="Title is required")
    
    args = parser.parse_args()

    if args.mode == "table" :
        if args.dateMode == "on" :
            if args.filename:
                with open(args.filename) as f:
                    for line in f:
                        label, value, date = line.strip().split("\t")
                        lab_val.append((label, float(value), date))

            lab_val.sort(key=lambda x: x[1])
            lab_val.reverse()

            for i in range(len(lab_val)):
                labels.append(lab_val[i][0])
                values.append(lab_val[i][1])
                dates.append(lab_val[i][2])

            table = PrettyTable(['Coin', args.value_column, 'Date'])
            table.title = args.title

            for i in range(len(labels)):
                table.add_row([labels[i], values[i], dates[i]])
        elif args.dateMode == "off" :
            if args.filename:
                with open(args.filename) as f:
                    for line in f:
                        label, value = line.strip().split("\t")
                        lab_val.append((label, float(value)))

            lab_val.sort(key=lambda x: x[1])
            lab_val.reverse()

            for i in range(len(lab_val)):
                labels.append(lab_val[i][0])
                values.append(lab_val[i][1])

            table = PrettyTable(['Coin', args.value_column ])
            table.title = args.title

            for i in range(len(labels)):
                table.add_row([labels[i], values[i]])

        with open(args.filename_out, 'w') as f:
            f.write(table.get_string())
        
    elif args.mode == "bar-plot" :

        names = []
        values = []

        number_of_colors = 100

        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                    for i in range(number_of_colors)]

        if args.filename:
            with open(args.filename) as f:
                for line in f:
                    if args.dateMode == "on" :
                        label, value , date = line.strip().split("\t")
                    elif args.dateMode == "off" :
                        label, value  = line.strip().split("\t")
                    names.append(label)
                    values.append(round(float(value), 2))

        bars = plt.bar(names, height=values, width=.4)

        xlocs, xlabs = plt.xticks()

        # reference x so you don't need to change the range each time x changes
        xlocs=[i for i in names]
        xlabs=[i for i in names]

        plt.xlabel('Crypto')
        plt.ylabel('Value')
        plt.xticks(xlocs, xlabs)
        plt.title(args.title)

        arrData = np.array(names)

        for i in range(arrData.size) :
            yval = bars[i].get_height()
            plt.text(bars[i].get_x(), yval + .005, yval)
            bars[i].set_color(color[i])

        plt.yscale("log") 
        plt.savefig(args.filename_out)
