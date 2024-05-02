import numpy as np

data = np.array(list(map(int, input("Please, enter the x vector:").split())))

# data[1:] != data[:-1] is an array with len = len(data) - 1, 
# which contains boolean values of condition "is next number is unequal to previous?" excluding the last number
# Then I take only indexes of the data array, that aren't paiwise unequal using "where" 
# and add the last element of data array 
# diff is the same as [array[i + 1] - array[i] for i in range(len(array) - 1)].

indexes = np.append(np.where(data[1:] != data[:-1]), len(data) - 1)
difference = np.diff(np.append(-1, indexes))       

print(data[indexes])
print(difference)