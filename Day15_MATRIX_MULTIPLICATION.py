'''
Day15 :- Matrix multiplicaion
Difficulty :- Medium
Concepts :- 2D Lists , Nested loops 
Approach 
-> Input both matrices
-> Create result matrix with 0 values
-> Use three loops (i, j, k)
    i → row of first matrix
    j → column of second matrix
    k → for multiplication
->Multiply row elements with column elements
    result[i][j] = Σ (matrix1[i][k] * matrix2[k][j])
->Add all products → store in result

'''
# Input number of rows
rows = int(input("Enter number of rows: "))
# Input number of columns
cols = int(input("Enter number of columns: "))

matrix1 = []                     # Initialize matrix1
matrix2 = []                     # Initialize matrix2

print("Enter elements of first matrix:")

for i in range(rows):            # Loop for rows
    row = []                     # Temporary list to store one row
    for j in range(cols):        # Loop for columns
        element = int(input())   # Take element input
        row.append(element)      # Add element to row
    matrix1.append(row)          # Add completed row to matrix1
   

print("Enter elements of second matrix:")

for i in range(rows):            # Loop for rows
    row = []                     # Temporary list to store one row
    for j in range(cols):        # Loop for columns
        element = int(input())   # Take element input
        row.append(element)      # Add element to row
    matrix1.append(row)          # Add completed row to matrix2
    

result = []                      # Initialize result matrix

for i in range(rows):            # Loop through rows of matrix1
    row = []                     # Temporary row for result
    for j in range(cols):        # Loop through columns of matrix2
        sum = 0                  # Initialize sum for each position
        
        for k in range(cols):    # Loop for multiplication
            
            # Multiply corresponding elements and add
            sum = sum + matrix1[i][k] * matrix2[k][j]
        row.append(sum)          # Store computed value in row
    result.append(row)           # Add completed row to result matrix

print("Multiplication of matrices:")

for r in result:
    print(r)