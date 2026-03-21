'''
Day08:- To find GCD and LCM 
Difficulty:- Medium
Concept:- Loops (while)
• Conditional statements (if-else)
• Euclidean Algorithm
• Arithmetic operations
• Integer division (//)
Approach:
Step 1 :For GCD:
Take two numbers
Use repeated subtraction method
Keep subtracting smaller from larger
When both become equal → that is GCD
For LCM:

Use formula:

LCM = (n1 × n2) / GCD

 '''
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

a = n1
b = n2

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

gcd = a  

lcm = (n1 * n2) // gcd

print(f"GCD of {n1} and {n2} is: {gcd}")
print(f"LCM of {n1} and {n2} is: {lcm}")