import matplotlib.pyplot as plt
import numpy

labels = ['Frogs', 'Hogs', 'Dogs', 'Cats']
sizes = numpy.array([5860.0, 677.0, 3200.0, 4000.0])
colors = ['yellowgreen', 'gold', 'lightskyblue', 'darkred']


def absolute_value(val):
    a = numpy.round(val/100.*sizes.sum(), 0)
    return a


plt.pie(sizes, labels=labels, colors=colors, autopct=absolute_value, shadow=True)

plt.axis('equal')
plt.savefig('./test_plot_pie.png')