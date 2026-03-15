'''Matrix multiplication'''
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
        row.append(0)
    result.append(row)

for i in range(R):
    row = []
    for j in range(C):
        sum = 0
        for k in range(c):
        sum = sum + matrix1[i][k] * matrix2[k][j] 
        row.append(sum)
    result.append(row)

print("multiplication of matrices : ")
``
for r in result:
    print(r)