'''Program to convert a binary number to a decimal number'''

B = input("Enter a binary number: ")

decimal = 0
length = len(B)

for i in range(length):
    digit = int(B[i])
    power = length - i - 1
    decimal =decimal + digit * pow(2, power)

print("Decimal number is:", decimal)