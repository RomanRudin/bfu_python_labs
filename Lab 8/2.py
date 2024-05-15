import matplotlib.pylab as plt 
import numpy as np

ratio = ((3, 2), (3, 4), (5, 4), (5, 6))

t = np.linspace(-4, 4, num=500)
x = np.array([np.sin(a * t) for a, b in ratio])
y = np.array([np.sin(b * t) for a, b in ratio])

for i, name in enumerate(ratio):
    plt.plot(x[i], y[i], label=f"ratio = {name}")
    plt.show()

