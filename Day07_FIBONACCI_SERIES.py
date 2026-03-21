''' Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''

n=int(input("Enter number of terms : "))
a=0
b=1

if n <= 0 :
    print("Enter a positive number")

elif n == 1:
    print("Fibonacci series")
    print(a)

else:
    print("fibonacci series")
    for i in range (n):
        print(a)
        c=a+b
        a=b
        b=c