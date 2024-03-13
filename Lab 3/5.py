def determinant(data):
    assert len(data) > 2
    if len(data) == 2:
        return data[0][0] * data[1][1] - data[1][0] * data[0][1]
    det = 0
    for i, elem in enumerate(data[0]):
        new_data = []
        for index1 in range(len(data)):
            if index1 != i:
                new_data.append(data[i])
                new_data[index1].pop(i)
        det += (-1) ** (i + 1) * elem * determinant(new_data)
    return det

n = int(input("Please, enter the size of the matrix: "))
print("Please, enter the matrix:")
a = []
for i in range(3):
    a.append(list(map(int, input().split())))
if not determinant(a):
    print("Yes")