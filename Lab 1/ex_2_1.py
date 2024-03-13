# n = int(input("Please, enter the n: "))
n = 21
print()

for i in range(1, n+1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    print(line)