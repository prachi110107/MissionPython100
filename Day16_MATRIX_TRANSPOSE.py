'''
Day16 :- Matrix transpose
Difficulty :- Easy
Concepts :- 2D Lists , Nested loops , Index swapping (i <-> j)
Approach
Step 1 : Input matrice
Step 2 : Create new matrix of size (cols × rows)
Step 3 : Use two loops (i, j)
Step 4 : Swap indices:
         transpose[j][i] = matrix[i][j]

'''
# Input number of rows
rows = int(input("Enter number of rows: "))
# Input number of columns
cols = int(input("Enter number of columns: "))

matrix = []                                # Intialize matrix
transpose = []                             # Intialize transpose

print("Enter elements of matrix:")

for i in range(rows):                      # Loop through rows
            row = []                       # Temporary list for one row
            for j in range(cols):          # Loop through columns
                element = int(input())     # Take input element
                row.append(element)        # Add element to row
            matrix.append(row)             # Add completed row to matrix

for i in range(cols):                      # Loop will run cols times (new rows)
    row = []                               # Temporary row for transpose
    for j in range(rows):                  # Loop will run rows times (new columns)
        
        row.append(matrix[j][i])           # Swap row and column index 
    transpose.append(row)                  # Add completed row to transpose matrix

print("Transpose of matrix : ")

for r in transpose:               
    print(r)                       
           