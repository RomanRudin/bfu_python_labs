n = int(input("Please, enter the n: "))
print()

max_string = ""
for i in range(1, n + 1):
    max_string += str(i)
extra_digits = len(max_string) - n

for i in range(1, n+1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    line = " " * extra_digits + line 
    extra_digits -= len(str(i)) - 1
    print(line)