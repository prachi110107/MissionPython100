'''Program to find GCD and LCM'''
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