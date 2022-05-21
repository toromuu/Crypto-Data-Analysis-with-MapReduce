import numpy as np
import matplotlib.pyplot as plt

x=range(5)
y=np.random.rand(5)

#plot3: barh with correct order: top-down y axis
plt.figure()
plt.barh(x,y)
plt.gca().invert_yaxis()

plt.show()