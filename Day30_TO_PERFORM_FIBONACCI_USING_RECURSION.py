'''
Day30 :- Program to perform fibonacci using recursion 
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
     
    return palindrome(n[1:-1])                      # Recursive call 


# Take number of inputs from user
n=int(input("Enter number of terms : "))

# Initialize first two Fibonacci numbers
a=0          # first term
b=1          # second term

# Check for invalid input
if n <= 0 :
    print("Enter a positive number")

# If only one term is required
elif n == 1:
    print("Fibonacci series")
    print(a)  # Print only the first term

# If more than one term
else:
    print("fibonacci series")
    for i in range (n):             # Loop runs n times 
        print(a)                    # Print current term
        c=a+b                       # Print next term
       
       # Update values
        a=b                         # Shift b to a
        b=c                         # Shift c to b