'''Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''
n = int(input("Enter number of rows : "))

print("\n TRIANGLE :\n")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


print("\n PYRAMID :\n")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


print("\n INVERTED PYRAMID :\n")
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()