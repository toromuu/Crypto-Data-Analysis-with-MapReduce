import argparse
from prettytable import PrettyTable

if __name__ == '__main__':
    labels = []
    values = []
    lab_val = []

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed")
    args = parser.parse_args()

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

    table = PrettyTable(['Moneda', 'Valor'])
    for i in range(len(labels)):
        table.add_row([labels[i], values[i]])

    with open('query1_s3.txt', 'w') as f:
        f.write(table.get_string())