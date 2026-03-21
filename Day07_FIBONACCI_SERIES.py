''' 
Day07:- Fibonacc series
Difficulty:- Medium
Concept:- Variables , Loop , Conditional statements , Sequence generation
Approach:
Step 1 : Take number of terms from user
Step 2 : Initialize first two numbers → 0 and 1
Step 3 : Handle special cases:
            If n <= 0 → invalid input
            If n == 1 → print only first number
Step 4 : For remaining cases : 
         Print current number
         Generate next term using : next = a + b
         Update values (a = b, b = next)

'''

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