'''
Day25:- Perform basic recursion
Difficulty:- Medium
Concept:- Recursion = Function calling itself
A recursive function has 2 main parts:
Base Case → Stops recursion  ,  Recursive Case → Function calls itself
Approach:
Step 1 : Take input from user
Step 2 : Define recursive function
Step 3 : If number is 0 or 1 → return 1 (base case)
Step 4 : Else → return n × factorial(n-1)
Step 5 : Print result

'''


def factorial(n) :                                 # Defining recursive function

    if n == 0 or n == 1 :                          # Base case
        return 1
    
    else :                                         # Recursive case
        return n * factorial(n-1)                  # Function calls itself with smaller value
    

n = int(input("Enter a number : "))                # Take input from user

if n < 0 :                                         # Negative number checking
    print("factorial of given number does not exixts")
else :
    result = factorial(n)                          # Call function and store result
    print("Factorial of", n , "is" , result)       # Print result
     
