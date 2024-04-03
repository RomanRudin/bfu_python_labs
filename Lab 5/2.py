data = []   
with open("Lab 5/2.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()
data.sort()
with open("Lab 5/2.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(data))