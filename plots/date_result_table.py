import argparse
from prettytable import PrettyTable

if __name__ == '__main__':
    labels = []
    values = []
    dates = []
    lab_val = []

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed with extension")
    parser.add_argument("filename_out", help="The filename result with extension")
    args = parser.parse_args()

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

    table = PrettyTable(['Moneda', 'Valor', 'Fecha'])
    for i in range(len(labels)):
        table.add_row([labels[i], values[i], dates[i]])

    with open(args.filename_out, 'w') as f:
        f.write(table.get_string())