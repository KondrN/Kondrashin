import matplotlib.pyplot as plt
import  numpy as np
theta = np.linspace(0, 90,150)
r= theta/72
plt.figure(figsize=(6, 6))
plt.axes(projection='polar')
plt.scatter(theta, r,s=400*r**2,c=theta,cmap='hsv',alpha=0.8)
plt.show()
