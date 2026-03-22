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


n = int(input("Enter a number : "))

reverse = 0
while n > 0:
    digit = n % 10     
    reverse = reverse * 10 + digit
    n = n // 10           
print("Reversed Number is:", reverse)