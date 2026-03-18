'''Program to convert decimal to binary'''
decimal = int(input("Enter a decimal number : "))

binary = ""
temp = decimal
count = 0
while temp > 0:
    temp = temp// 2
    count += 1


for i in range(count):
    remainder = decimal % 2
    binary += str(remainder)
    decimal = decimal // 2

print("Binary number is :", binary)