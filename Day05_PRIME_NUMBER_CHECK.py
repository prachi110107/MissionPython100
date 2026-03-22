'''
Day05:- Prime number check
Difficulty:- Medium
Concept:- A Prime Number is a number that is divisible only by: 1 and itself
Approach:
Step 1 : Take number from user
Step 2 : Loop from 2 to n-1
Step 3 : Check if number is divisible
         If divisible → not prime
         If no divisor found → prime

'''

# Ask user to enter a number
n=int(input("Enter number of your choice : "))

for i in range(2,n):                                # Loop runs from 2 to n-1
    if n % i == 0:                                  # Check if n divisble by i or not 
        print("It's not a prime number")            # If divisible , then not a prime number

else:                                               # If not divisible , then is a prime number
    print("It's a prime number")              
