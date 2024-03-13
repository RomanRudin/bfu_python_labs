data = {}
a = list(input("Please, enter the line: ").split())
for elem in a:
	if elem in data:
		data[elem] += 1
	else:
		data[elem] = 1
answer = [elem for elem in data.values()]
for i in answer:
	print(i, end="\t")
