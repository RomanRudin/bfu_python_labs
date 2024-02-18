a = list(map(int, input("Please, input numbers: ").split()))
answer = 0
for i in a:
    if a.count(i) > 1:
        answer = max(answer, a.count(i))
print(f"There are {answer} same numbers in given array.")