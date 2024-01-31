n = int(input("Please, enter the n number: "))
print()

max_string = ""
for i in range(1, n + 1):
    max_string += str(i)
max_len = len(max_string) 

for i in range(1, n + 1):
    line = ""
    for j in range(i, 0, -1):
        line += str(j)
    line = " " * (max_len - len(line)) + line   
    for j in range(2, i + 1):
        line += str(j) 
    print(line)