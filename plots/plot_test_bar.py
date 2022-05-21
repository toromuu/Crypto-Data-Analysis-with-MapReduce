import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

Months = ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

P = [220, 120, 50, 24, 54, 72]
T = [7, 12, 18, 24, 14, 5]

ax.bar(np.arange(1.75, len(P)+1.75), P, 0.5, color='k')
ax.set_ylabel("Precipitation, mm", fontsize=12)
ax.set_xlabel("2013", fontsize=12)

plt.xticks(np.arange(1.75, len(P)+1.75), Months)
plt.xlim(1, 7.5)

plt.tight_layout()

plt.savefig('./test_plot_bar.png')