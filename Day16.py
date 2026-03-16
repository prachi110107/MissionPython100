'''Matrix transpose'''
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
transpose = []

print("Enter elements of matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix.append(row)

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)  

print("Transpose of matrix : ")
for r in transpose :
    print(r)