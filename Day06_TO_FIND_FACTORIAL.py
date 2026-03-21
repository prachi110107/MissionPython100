'''Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''

n=int(input("Enter a number : "))

if n < 0 :
    print("Factorial does not exist")

elif n == 0 :
    print("Factorial of zero is 1")

else:
    factorial = 1
    for i in range (1,n +1):
        factorial = factorial * i
        
    print("Factorial of" , n , "is" , factorial)