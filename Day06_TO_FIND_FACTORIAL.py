'''
Day06:- To find factorial of a given number
Difficulty:- Easy 
Concept:- Factorial of a number means:
          n! = n × (n-1) × (n-2) × ... × 1
Approach:
Step 1 : Take input number from user
Step 2 : Check special cases:
         If number < 0 → factorial does not exist
         If number = 0 → factorial is 1
Step 3 : Otherwise:
Initialize factorial = 1
Use loop from 1 to n
Multiply each number
Step 4 : Print final result

'''

n=int(input("Enter a number : "))                   # Ask user to enter a number

if n < 0 :                                          # If entered number less then 0 then factorial does not exists
    print("Factorial does not exist")

elif n == 0 :                                       # If entered number is zero than factorial is one
    print("Factorial of zero is 1")

else:                                              # If entered number is greater than 1
    factorial = 1
    for i in range (1,n +1):
        factorial = factorial * i
        
    print("Factorial of" , n , "is" , factorial)   # print factorial