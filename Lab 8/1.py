import matplotlib.pylab as plt 
import scipy
import numpy as np
import scipy.special

max_n = 7
figure, axis = plt.subplots(1, 1)
x = np.linspace(-1, 1)
y = np.array(list(scipy.special.lpn(max_n, xi)[0] for xi in x)).T


for i, yi in enumerate(y):
    axis.plot(x, yi, label=f"n = {i}")

plt.title("Полиндромы Лежандра")
axis.legend()
axis.grid()
plt.show()