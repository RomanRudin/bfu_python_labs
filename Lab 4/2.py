a = set(map(int, input("input data: ").strip("()").replace(',', '').split()))
b = set(map(int, input().strip("()").replace(',', '').split()))
print(f'Is {a} the subset of {b}: \n{str(a.issubset(b)).upper()}')