import matplotlib.pyplot as plt
import numpy
import sys

labels = []
#values = numpy.array([5860.0, 677.0, 3200.0, 4000.0])
values = []

for line in sys.stdin:
    data = line.strip().split("\t")
    name, value = data
    labels.append(name)
    values.append(value)

auxValues = numpy.array(values)
colors = ['yellowgreen', 'gold', 'lightskyblue', 'darkred']


def absolute_value(val):
    a = numpy.round(val/100.*sizes.sum(), 0)
    return a

plt.pie(sizes, labels=labels, colors=colors, autopct=absolute_value, shadow=True)

plt.axis('equal')
plt.savefig('./test_plot_pie.png')