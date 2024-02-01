# n = int(input("Please, enter the n number: "))
n = 21
print()
    

max_string = ""
for i in range(n, 0, -1):
    max_string += str(i)
extra_digits = len(max_string)

for i in range(1, n + 1):
    line = ""
    for j in range(i, 0, -1):
        line += str(j) 
    line = " " * (extra_digits - len(line)) + line 
    for j in range(2, i + 1):
        line += str(j) 
    print(line)