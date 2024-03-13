a = input("Please, enter the code from first exersize: ")
answer = ""
i = 0
while i < len(a):
	if i < len(a) - 1:
		if a[i + 1].isdigit():
			answer += a[i] * int(a[i + 1])
			i+= 1
		else:
			answer += a[i]
	else:
		answer += a[i]
	i += 1
print(answer)
