'''
Day34:- Move zeros to end (Two pointer technique)
Difficulty:- Medium
Concept:- Move all 0's to the end , Maintain order of non-zero elements
Approach:
Step 1 : Take input list
Step 2 : Initialize pointer j = 0
Step 3 : Traverse list using i
Step 4 : If element ≠ 0:
         Swap arr[i] with arr[j]
         Increment j
Step 5 : Print updated list

'''
# Ask user to give input 
arr = list(map(int, input("Enter elements separated by space: ").split()))

j = 0                                             # Initialize pointer for non-zero position

for i in range(len(arr)):                         # Traverse array
    
    if arr[i] != 0:                               # If element is not zero
        
        arr[i] , arr[j] = arr[j] , arr[i]         # Swap elements
        
        j += 1                                    # Move pointer forward

print("Array after moving zeros:", arr)           # Print result