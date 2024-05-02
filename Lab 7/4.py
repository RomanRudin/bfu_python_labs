import numpy as np

data = np.array(list(map(int, input("Please, enter the x vector:").split())))

print(np.max(data[np.where(np.diff(np.append(data[0], data)) == data)]))