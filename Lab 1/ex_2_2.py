n = int(input("Please, enter the n number: "))
print()

max_string = ""
for i in range(n, 0, -1):
    max_string += str(i)
for i in range(2, n + 1):
    max_string += str(i)
extra_digits = len(max_string) - n * 2 - 1
print(extra_digits)

for i in range(1, n + 1):
    line = ""
    for j in range(i, 0, -1):
        line += str(j) 
    for j in range(2, i + 1):
        line += str(j) 
    line = " " * (extra_digits - len(line)) + line  
    extra_digits -= (len(str(i)) - 1) * 2
    print(line)
    print(extra_digits)
