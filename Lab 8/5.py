import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(1, 2, subplot_kw={'projection': '3d'})

x1 = np.linspace(0, 10, 100)
y1 = np.random.normal(0, 1, 100)
z1 = np.square(y1)

axes[0].plot_trisurf(x1, y1, z1)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_zlabel('z')

x2 = np.linspace(0, 10, 100)
y2 = np.random.normal(0, 1, 100)
z2 = np.square(y2)

axes[1].plot_trisurf(x2, y2, z2)
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_zlabel('Log(z)')
axes[1].set_zscale('log')

plt.show()