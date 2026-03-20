'''
Day20 :- Binary Search
Difficulty :- Medium
Concepts :- Sorted list , Divide and conquer , Loop + condition , Index calculation
Approach 
Step 1 : The list must be sorted
Step 2 : Initialize pointers
        low = 0  
        high = n - 1
Step 3 : Find middle element
        mid = (low + high) // 2
Step 4 : Compare with key
        Case 1:
        If arr[mid] == key
        Element found → stop    

        Case 2:
        If key < arr[mid]
        Search in left half
        high = mid - 1
        
        Case 3:
        If key > arr[mid]
        Search in right half
        low = mid + 1
Step 5 : Repeat and Continue until Element is found OR
        low > high (not found)

'''
# First input list
lst = input("Enter elements separated by space: ").split()

# Convert that input list into integers
lst = [int(x) for x in lst]

# Sort the list 
lst.sort()

# Enter element which you want to search 
key = int(input("Enter element to search: "))

low = 0                            # Initialize starting index of list
high = len(lst) - 1                # Initialize ending index of list

# Use flag variable to check if element is found or not
found = False

while low <= high :               # Loop runs until valid search space exists
    mid = (low + high) // 2       # Find middle index of current search space
    if lst[mid] == key :          # Check if middle element is equal to key
        print("element found")
        found = True
        break 
    elif lst[mid] > key :         # If key is smaller than middle element
        high = mid -1             # Move to left half
    else:
        lst[mid] < key            # If key is greater than middle element
        low = mid + 1             # Move to right half

# After loop ends, check if element was found
if not found :
        print("element not found")