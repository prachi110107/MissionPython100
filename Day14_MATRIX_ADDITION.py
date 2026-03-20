'''
Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : Take two matrices and create empty result matrix
Step 2 : Use two loops (i, j) to access each position
Step 3 : Add corresponding elements → matrix1[i][j] + matrix2[i][j]
Step 4 : Store result in same position

'''
# Input number of rows
R = int(input("Enter number of rows : "))
# Input number of columns
C = int(input("Enter number of columns : "))

matrix1 = []                     # Initialize matrix1
matrix2 = []                     # Initialize matrix2

print("Enter elements of first matrix :")

for i in range(R):               # Loop for rows
    row = []                     # Temporary list to store one row
    for j in range(C):           # Loop for columns
        element = int(input())   # Take element input
        row.append(element)      # Add element to row
    matrix1.append(row)          # Add completed row to matrix1
    

print("Enter elements of second matrix :")

for i in range(R):               # Loop for rows
    row = []                     # Temporary list to store one row
    for j in range(C):           # Loop for columns
        element = int(input())   # Take element input
        row.append(element)      # Add element to row
    matrix2.append(row)          # Add completed row to matrix2
    

result = []                      # Initialize result matrix

for i in range(R):               # Loop through rows
    row = []                     # Temporary row for result
    for j in range(C):           # Loop through columns
        
        # Add corresponding elements of both matrices
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)           # Add completed row to result matrix

print("Sum of matrices : ")

for r in result:
    print(r)