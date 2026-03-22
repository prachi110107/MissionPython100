'''
Day02:- Reversing a number
Difficulty:- Easy 
Concept:- Loops (while, for) , Modulus (%) and Integer division (//) 
Approach:
Step 1 : Take input number
Step 2 : Extract last digit using % 10
Step 3 : Build reverse using:
         reverse = reverse * 10 + digit
         Remove last digit using // 10
Step 4 : Print reversed number

'''

# Ask user to enter a number   
n = int(input("Enter a number : "))

reverse = 0                                     # Initialize reverse

while n > 0:                                    # Reverse logic using while loop
    digit = n % 10                              # Get last digit
    reverse = reverse * 10 + digit              # Build reverse
    n = n // 10                                 # Remove last digit

# Print reverse number
print("Reversed Number is:", reverse)