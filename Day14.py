'''Matrix addition'''
R = int(input("Enter number of rows : "))
C = int(input("Enter number of columns : "))

matrix1 = []
matrix2 = []

print("Enter elements of first matrix :")

for i in range(R):
    row = []
    for j in range(C):
        element = int(input())
        row.append(element)
    matrix1.append(row)

print("Enter elements of second matrix :")

for i in range(R):
    row = []
    for j in range(C):
        element = int(input())
        row.append(element)
    matrix2.append(row)

result = []

for i in range(R):
    row = []
    for j in range(C):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Sum of matrices : ")

for r in result:
    print(r)