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