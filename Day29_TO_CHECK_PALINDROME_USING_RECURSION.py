'''
Day29 :- Program to check palindrome using recursion 
Difficulty :- Medium
Concepts :- 
A Palindrome is a string that reads same forward and backward
Using recursion: Compare first and last character , Then check remaining string
Approach 
Step 1 : Take number or string input
Step 2 : Define recursive function
Step 3 : Base case: If string length ≤ 1 → palindrome
Step 4 : Check: First char == last char
Step 5 : Recursive call on remaining string
Step 6 : Print result

'''

def palindrome(n) :                                 # Defining recursive function

    if len(n) <= 1:                                 # Base case , palindrome
        return True
    
    if n[0] != n[-1]:                               # Check first and last character , not palindrome
        return False                 
     
    return palindrome(n[1:-1])                   # Recursive call 


# Take input from user it can be a number or string
Value = input("Enter a number or string : ")

# Check if it is a number 
if Value.isdigit():

    n = int(Value)                  # If yes , then convert it into an integer
    original = n
    reverse = 0

    while n > 0:                    # Reverse number concept
        digit = n % 10     
        reverse = reverse * 10 + digit
        n = n // 10   

    if original == reverse :        # Compare original and reverse
        print("It is a palindrome number")
    else:
        print("It is NOT a palindrome number")

else:                               # If input is a string
    original = Value
    reverse = "" 
    for ch in original:              # Reverse string using loop
        reverse = ch + reverse       # add character in front
        

# Compare reverse and original       
    if original == reverse:
        print("It is a Palindrome String")
    else:
        print("It is NOT a Palindrome String")