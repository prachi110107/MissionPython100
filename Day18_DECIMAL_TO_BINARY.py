'''
Day18:- Decimal to binary
Difficulty:-Medium
Concept:- Division by 2 , Remainders 
Approach:
Step 1 : Take decimal number
Step 2 : Divide by 2 repeatedly
Step 3 : Store remainders
Step 4 : Reverse result

'''
decimal = int(input("Enter a decimal number : "))

binary = ""                                 # Initialize binary as empty string
temp = decimal                              # Store original value in temp for counting
count = 0                                   # Initialize counter to count number of steps


while temp > 0:                             # Count how many times number can be divided by 2
    temp = temp// 2                         # Divide number by 2
    count += 1                              # Increase count


for i in range(count):                      # Use for loop to generate binary digits
    remainder = decimal % 2                 # Find remainder (0 or 1)
    binary += str(remainder)                # Add remainder at beginning of binary string
    decimal = decimal // 2                  # Update decimal by dividing by 2

print("Binary number is :", binary)