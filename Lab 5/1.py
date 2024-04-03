prod = 1
with open("Lab 5/input.txt", "r", encoding="utf-8") as file:
    data = list(map(int, file.readline().split()))
    for num in data:
        prod *= num
with open("Lab 5/output.txt", "w", encoding="utf-8") as file:
    file.write(str(prod))