'''Matrix multiplication'''
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []

print("Enter elements of first matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix1.append(row)

print("Enter elements of second matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix2.append(row)

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        sum = 0
        for k in range(cols):
            sum = sum + matrix1[i][k] * matrix2[k][j]
        row.append(sum)
    result.append(row)

print("Multiplication of matrices:")

for r in result:
    print(r)