n = int(input("Please, enter the number: "))
assert n > 0
data = ["1"]
previous = [1]
print("The answer is: ")
for i in range(2, n+1):
    current = [1]
    for j in range(1, i-1):
        current.append(previous[j-1] + previous[j])
    current.append(1)
    previous = current
    data.append(" ".join([str(sym) for sym in current]))

max_len = len(data[-1])
for i in range(n):
    print(" " * ((max_len - len(data[i])) // 2) + data[i])
