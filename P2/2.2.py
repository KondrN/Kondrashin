import matplotlib.pyplot as plt
import  numpy as np
x = np.linspace(-10, 10, 250)
y= np.sin(x)
plt.figure(figsize=(10, 5))
plt.scatter(x, y)

plt.scatter(x, y,s=300,marker='s',c='violet',lw=2,edgecolor='black',hatch='**')

plt.title(label='$sin(x)$ with random noise', fontsize=20 )
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)

plt.xticks(ticks=np.arange(-10, 11, 2) )
plt.yticks(ticks=np.arange(-1.5, 2,0.5),labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1])
plt.plot(x, y)
plt.show()
