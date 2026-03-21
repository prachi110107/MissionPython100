'''Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''

n=int(input("Enter number of your choice : "))
for i in range(2,n):
    if n % i == 0:
        print("It's not a prime number")
else:
    print("It's a prime number")
