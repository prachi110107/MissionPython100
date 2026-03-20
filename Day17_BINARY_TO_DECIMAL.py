'''
Day17:- Binary to decimal 
Difficulty:- Easy 
Concept:- Number system , Powers of 2 , Strings and indexing , Loop 
Approach:
Step 1 : Take binary number as string
Step 2 : Multiply each digit with 2^power
Step 3 : Increase power each step
Step 4 : Add all values

'''

B = input("Enter a binary number: ")

decimal = 0                                     # Initialize decimal result as 0
length = len(B)                                 # Find length of binary string

for i in range(length):                         # Loop through each digit of binary number
    digit = int(B[i])                           # Convert current character into integer


    # Calculate power based on position
    # Leftmost digit has highest power
    power = length - i - 1


    decimal =decimal + digit * pow(2, power)     # Multiply digit with 2^power and add to decimal

print("Decimal number is:", decimal)