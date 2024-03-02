# importing libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# defining surface and axes
x = np.outer(np.linspace(0, 100, 1000), np.ones(10))
y = np.outer(np.linspace(0, 100, 1000), np.ones(10))
z = x**4+y**4

fig = plt.figure()

# syntax for 3-D plotting
ax = plt.axes(projection='3d'),

# syntax for plotting
ax.plot_surface(x, y, z, cmap='viridis',edgecolor='green')
ax.set_title('Surface plot geeks for geeks')
plt.show()