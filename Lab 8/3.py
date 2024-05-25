import matplotlib.pylab as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

figure = plt.figure()

ratio = np.linspace(0, 10, num=1000)
t = np.linspace(-4, 4, num=500)
x = np.array([np.sin(i * t) for i in ratio])
y = np.array(list(np.sin(10 * t) for _ in ratio))

def animate(i):
    figure.clear()
    plt.plot(x[i], y[i])

anim = FuncAnimation(figure, animate, frames=1000, interval=10)
plt.show()