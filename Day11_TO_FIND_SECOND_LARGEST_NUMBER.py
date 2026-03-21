'''
Day11:- To find second largest number 
Difficulty:- Easy 
Concept:- Lists , User input , Loop , Sorting , Indexing 
Approach:
Step 1 : Take number of elements from user
Step 2 : Store elements in a list
Step 3 : Sort the list in ascending order
Step 4 : Access second last element using indexing
Step 5 : Print result

'''

# Take number of inputs from user
n=int(input("Enter number of elements : "))

numbers=[]                                           # Create empty list 
for i in range(n):                                   # Loop runs n times
    num=int(input("Enter elements : "))              # Take input
    numbers.append(num)                              # Add input to the list 
numbers.sort()                                       # Sort the list in ascending order

print("Second largest number is : " , numbers[-2])   # -2 gives second largest element while -1 gives largest element
