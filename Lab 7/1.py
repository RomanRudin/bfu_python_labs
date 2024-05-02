import numpy as np

with open("1.txt", 'r', encoding="utf-8") as file:
    a = np.array([list(map(int, x.split(","))) for x in file.read().split()])
print("Sum of all elements:", a.sum())
print("Largest element:", a.max())
print("Smallest elements:", a.min())