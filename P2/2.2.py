import matplotlib.pyplot as plt
import  numpy as np
x = np.linspace(-10, 10, 1000)
target_noise_db = 10

# Convert to linear Watt units
target_noise_watts = 1

# Generate noise samples
mean_noise = 0
y= np.sin(x)
noise_volts = np.random.normal(mean_noise, 1/10, len(y))
z=y+noise_volts
plt.figure(figsize=(10, 5))
plt.scatter(x, z)

plt.scatter(x, z,s=300,marker='s',c='violet',lw=2,edgecolor='black',hatch='**')

plt.title(label='$sin(x)$ with random noise', fontsize=20 )
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)

plt.xticks(ticks=np.arange(-10, 11, 2) )
plt.yticks(ticks=np.arange(-1.5, 2,0.5),labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1])
plt.plot(x, z)
plt.show()
