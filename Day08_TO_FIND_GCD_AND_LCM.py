'''
Day08:- To find GCD and LCM 
Difficulty:- Medium
Concept:- Loops , Conditional statements , Euclidean Algorithm , Arithmetic operations , Integer division (//)
Approach:
For GCD:
Step 1 : Take two numbers
Step 2 : Use repeated subtraction method
Step 3 : Keep subtracting smaller from larger
Step 4 : When both become equal → that is GCD
For LCM:
Use formula : LCM = (n1 * n2) // GCD

 '''
n1 = int(input("Enter first number : "))          # Ask user to input first number 
n2 = int(input("Enter second number : "))         # Ask user to input second number

# Store original values
a = n1
b = n2

while a != b:                                      # Loop runs until both a and b becomes equal
    if a > b:                                      # If a is greater
        a = a - b
    else:                                          # If b is greater
        b = b - a

gcd = a                                            # when loop ends both a and b are  equal -> GCD

lcm = (n1 * n2) // gcd                             # To Calculate LCM 


# Print results
print(f"GCD of {n1} and {n2} is: {gcd}")
print(f"LCM of {n1} and {n2} is: {lcm}")