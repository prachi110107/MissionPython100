'''Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''
n = int(input("Enter a number : "))

reverse = 0
while n > 0:
    digit = n % 10     
    reverse = reverse * 10 + digit
    n = n // 10           
print("Reversed Number is:", reverse)