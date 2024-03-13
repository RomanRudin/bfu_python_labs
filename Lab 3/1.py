a = input("Please, enter the string: ")
answer = ""
i = 0
while i < len(a):
	if i == len(a) - 1:
		answer += a[i]
		break
	counter = 1
	while (a[i] == a[counter + i]):
		counter += 1
		if (counter + i >= len(a) ):
			break
	answer += a[i]
	if counter != 1:
		answer += str(counter)
		i += counter - 1
	i += 1
print("The shortened variant is:", answer)