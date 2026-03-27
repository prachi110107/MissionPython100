'''
Day27 :- Program to demostrate power function (exponent) using recursion 
Difficulty :- Medium
Concepts :- 
a^b = a * a * a * ....(b times)
using recursion : a^b = a * a^(b-1)
Approach 
Step 1 : Take base (a) and exponent (b) as input from user
Step 2 : Define recursive function
Step 3 : Base case → if exponent = 0 , return 1
Step 4 : Recursive case → sum = return a * power(a,b-1)
Step 5 : Print result

'''

def power_function(a,b) :                               # Defining recursive function

    if b == 0 :                                         # Base case
        return 1
    
    else :                                              # Recursive case
        return a * power_function(a,b-1)                # Multiply base with result of smaller problem
    

base = int(input("Enter base value : "))                # Take input from user
exponent = int(input("Enter exponent value : "))

if exponent < 0 :                                       # Negative exponent check
    result = 1 / power_function(base , -exponent)

else :
    result = power_function(base , exponent)            # Call function and store result

print("Result : " , result)                             # Print result
