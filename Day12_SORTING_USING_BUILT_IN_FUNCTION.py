'''
Day12:- Sorting using built in function
Difficulty:- Medium
Concept:- Lists , User input , Nested loops , Comparison , Swapping values , Basic sorting algorithm 
Approach:
Step 1 : Take number of elements from user
Step 2 : Store elements in a list
Step 3 : Use nested loops to compare elements
Step 4 : Swap elements if they are in wrong order
Step 5 : Print sorted list

 '''
# Take number of elements from user
n=int(input("Enter the no of elements : "))

numbers=[]                                     # Create empty list
for i in range(n):                             # loop runs n times
    num=int(input("Enter the elements : "))    # Take input
    numbers.append(num)                        # Add element to the list 

# Apply sorting using nested loops
for i in range(len(numbers)):                  # outer loop selects element
    # inner loop compares with next elements
    for j in range(i+1,len(numbers)):
        
        if numbers[i] > numbers[j]:             # Compare elements
            # Swap elements if in wrong order
            temp = numbers[i]                   # Store first value
            numbers[i] = numbers[j]             # Replace with smaller value
            numbers[j] = temp                   # Put stored value

print("Sorted list : " , numbers)               # Print sorted list