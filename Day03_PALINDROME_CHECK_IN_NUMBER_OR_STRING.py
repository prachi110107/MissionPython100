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

Value = input("Enter a number or string : ")
if Value.isdigit():

    n = int(Value)
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10     
        reverse = reverse * 10 + digit
        n = n // 10   

    if original == reverse :
        print("It is a palindrome number")
    else:
        print("It is NOT a palindrome number")

else:
    original = Value
    reverse = "" 
    for ch in original:
        reverse = ch + reverse
        
    if original == reverse:
        print("It is a Palindrome String")
    else:
        print("It is NOT a Palindrome String")