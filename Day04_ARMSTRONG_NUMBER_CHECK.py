'''
Day04:- Armstrong number check
Difficulty:- Easy 
Concept:- An Armstrong Number is a number where:
Sum of (each digit ^ number of digits) = original number
Approach:
Step 1 : Take input number
Step 2 : Store original number
Step 3 : Count number of digits
Step 4 : Extract each digit using % 10
Step 5 : Raise digit to power of total digits
Step 6 : Add to total
Step 7 : Remove last digit using // 10
Step 8 : Compare total with original number

'''

# Ask user to enter a number
n = int(input("Enter a number : "))

original = n                                   # Store original number for comparison later

digits = len(str(n))                           # convert to string to count digits
total = 0                                      # Intialize total sum
while n > 0:                                   # Extract digits using while loop
    digit = n % 10                             # Get last digit
    total = total + digit ** digits            # Add digit^digits to total
    n = n // 10                                # Remove last digit
    

# Check if armstrong or not
if total == original:
    print("It is an Armstrong Number")
else:
    print("It is NOT an Armstrong Number")