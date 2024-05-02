import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

vector = iris[:, 4]
vector = vector[np.append(np.where(vector[1:] != vector[:-1]), len(vector) - 1)]

print("Unique values:", vector)
print("Length of unique values:", len(vector))