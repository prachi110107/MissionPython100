'''
Day01:- To pint patters -> triangle , pyramid , inverted pyramid
Difficulty:- Easy 
Concept:- Nested loops (for) , Pattern printing , Use of range() , String formatting (end="") , Logic building with rows & columns
Approach:
1. Triangle
Outer loop → controls rows
Inner loop → prints stars equal to row number
2. Pyramid
First inner loop → prints spaces
Second inner loop → prints stars
Stars follow pattern: 2*i - 1
3. Inverted Pyramid
Same as pyramid but rows go in reverse
Stars decrease each row

'''

# Take input from user
n = int(input("Enter number of rows : "))

print("\n TRIANGLE :\n")

# Outer loop → controls rows
for i in range(1, n + 1):
    # Inner loop → prints stars
    for j in range(i):
        print("*", end="")           # Print stars in same line
    print()                          # Move to next line


print("\n PYRAMID :\n")
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()                           # Next line


print("\n INVERTED PYRAMID :\n")
# Outer loop in reverse
for i in range(n, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()                           # Next line