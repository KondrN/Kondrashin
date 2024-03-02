import matplotlib.pyplot as plt
import  numpy as np
import math

x = np.linspace(-10, 10, 1000)
y= (np.sin(2*x)**2)*(math.e**(((x+2)*(x+2))/100))
plt.figure(figsize=(8,3))
plt.grid(lw=0.5, ls='--')
plt.plot(x,y, lw = 4.0, color='red')
plt.plot(x, y)
plt.show()
