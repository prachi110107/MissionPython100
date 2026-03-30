'''
Day30 :- Program to perform fibonacci using recursion 
Difficulty :- Medium
Concepts :- 
A Palindrome is a string that reads same forward and backward
Using recursion: Compare first and last character , Then check remaining string
Approach 
Step 1 : Take number of terms from user
Step 2 : Define recursive function
Step 3 : Base case:
         if n == 0 → return 0
         if n == 1 → return 1
Step 4 : Recursive case:
         return fib(n-1) + fib(n-2)
Step 5 : Use loop to print series

'''


def fibonacci(n) :                                 # Defining recursive function

    if n == 0  :                                   # Base case 
        return 0
    
    if n == 1  :                                   
        return 1                
     
    return fibonacci(n-1) + fibonacci(n-2)         # Recursive call 



n=int(input("Enter number of terms : "))           # Take number of inputs from user

                                                   # Initialize first two Fibonacci numbers
a=0                                                # first term
b=1                                                # second term


if n <= 0 :                                        # If entered number is negative
    print("Enter a positive number")


elif n == 1:                                       # If only one term is required
    print("Fibonacci series")
    print(a)                                       # Print only the first term

else:                                              # If more than one term
    print("fibonacci series")
    for i in range (n):                            # Loop runs n times 
        print(a)                                   # Print current term
        c=a+b                                      # Print next term
       
                                                   # Update values
        a=b                                        # Shift b to a
        b=c                                        # Shift c to b