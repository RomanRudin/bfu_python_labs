import numpy as np

a = np.arange(16).reshape(4, 4)
b = np.array(a[0]) #or use copy(), I think
a[0], a[2] = a[2], b
print(a)