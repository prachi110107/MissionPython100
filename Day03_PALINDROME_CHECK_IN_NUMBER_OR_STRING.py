'''
Day03:- Palindrome check in number or string
Difficulty:- Easy 
Concept:- Loops (while, for) , Modulus (%) and Integer division (//) , Strings , Conditional statements (if-else) , isdigit() , String concatenation
Approach:
For Number: 
Convert input to integer
Reverse the number
Compare with original
For String:
Traverse characters
Reverse using loop
Compare with original

 '''

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