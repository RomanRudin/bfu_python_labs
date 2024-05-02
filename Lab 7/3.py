import numpy as np

data = np.random.normal(size=(10, 4))

print("Minimal value", data.max())
print("Maximal value", data.min())
print("Average value", data.sum() / (len(data) * len(data[0])))
print("Standard deviation", data.std())
first_five_rows = data[:5]
print("First five rows: \n", first_five_rows)