'''
Day19 :- Linear Search using list 
Difficulty :- Easy
Concepts :- Built-in functions
Approach 
Step 1 : Assume element not found (False)
Step 2 : Traverse list
Step 3 : If found → update to True
Step 4 : Break loop
Step 5 : After loop check flag

'''


# First input list
lst = input("Enter elements separated by space: ").split()

# Convert that input list into integers
lst = [int(x) for x in lst]

# Sort the list 
lst.sort()

# Enter element which you want to search 
key = int(input("Enter the number which is to be found : "))

# Use flag variable to check if element is found or not
found = False   

# Loop through list using index
for i in range (len(lst)):                                   # Loop from index 0 to last index
    if lst[i] == key:                                  # Check if current element matches the key
        print("Element found at position " , i + 1)
        found = True
        break

# After loop, check if element was not found
if not found:
    print("Element not found")   