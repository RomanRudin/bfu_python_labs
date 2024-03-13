data = {}
a = list(input().split())
counter = 0
for elem in a:
	if elem in data:
		data[elem] [1] += 1
	else:
		data[elem] = [counter, 1]
		counter += 1
answer = [elem for elem in data.values()]
answer.sort(key=lambda x: x[0])
for i in answer:
	print(i[1], end="\t")
