'''
Day26 :- Sum of digits using recursion 
Difficulty :- Medium
Concepts :- Recursion = function calling itself
To find sum of digits:
Take last digit → n % 10
Remove last digit → n // 10
Repeat until number becomes 0
Approach 
Step 1 : Take input from user
Step 2 : Define recursive function
Step 3 : Base case → if n == 0 return 0
Step 4 : Recursive case → sum = (last digit) + sum of remaining digits
Step 5 : Print result

'''

def sum_of_digits(n) :                             # Defining recursive function

    if n == 0 :                                    # Base case
        return 0
    
    else :                                         # Recursive case
        return (n % 10) + sum_of_digits(n // 10)   # Function calls itself with smaller value
    

n = int(input("Enter a number : "))                # Take input from user

if n < 0 :                                         # Negative number checking
    n = -n

else :
    result = sum_of_digits(n)                       # Call function and store result
    print("sum of digits", n , "is" , result)       # Print result