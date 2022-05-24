from matplotlib import pyplot as plt
import numpy as np

a = 3
b = 4
x = np.arange(-10,10,0.5)
y = a * x + b
plt.plot(x, y, 'r.-', label=f"y={a}x+{b}")
plt.legend(loc=2)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()