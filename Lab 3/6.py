data = input("Pleasem enter the line of text: ").strip().split()
answer = ""
for elem in data:
    answer += elem[0].capitalize()
print("The abbreviation is:", answer)