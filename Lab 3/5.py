# def determinant(data):
#     if len(data[0]) == 2:
#         return data[0][0] * data[1][1] - data[1][0] * data[0][1]
#     assert len(data) > 2
#     det = 0
#     print(data)
#     for i, elem in enumerate(data[0]):
#         print(i, elem)
#         new_data = []
#         for index1 in range(1, len(data)):
#                 new_data.append(data[index1])
#                 new_data[-1].pop(i)
#         print("new_data:", new_data)
#         det += (-1) ** (i + 1) * elem * determinant(new_data)
#     return det

def determinant(a):
    return a[0][0] * a[1][1] * a[2][2] + a[0][2] * a[1][0] * a[2][1] + a[0][1] * a[1][2] * a[2][0] - \
        a[0][2] * a[1][1] * a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1]

n = int(input("Please, enter the size of the matrix: "))
print("Please, enter the matrix:")
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    assert len(a[-1]) == n
if determinant(a):
    print("No, this matrix is not lineary dependant.")
else:
    print("Yes, this matrix is lineary dependant.")
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = str(a[i][j])
for i in a:
    print("\t".join(i))