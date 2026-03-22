'''
Day10:- Remove duplicates from list
Difficulty:- Medium
Concept:- Strings , Lists , Loops , Membership checking , Building new result
Approach:
For String:
Step 1 : Take input string
Step 2 : Traverse each character
Step 3 : Add only if not already present
Step 4 : Build new string
For List:
Step 1 : Take number of elements
Step 2 : Store elements in list
Step 3 : Traverse list
Step 4 : Add only unique elements to new list

'''

'''For string'''
S=input("Enter a string : ")     # Take string input
result = ""                      # Create empty result string
for ch in S :                    # Traverse each character
    if ch not in result :        # Check if character is not already in result
        result = result + ch     #  Add character to result

# Print results
print("Initial string : ", S)
print("Final string after removing duplicates : ", result)

'''For list'''  
# First input list
lst = input("Enter elements separated by space: ").split()

# Convert that input list into integers
lst = [int(x) for x in lst]

# Sort the list 
lst.sort()

new_list = []                              # Create empty list for unique elements
for num in lst :                           # Traverse the sorted list
    if num not in new_list:                # Add only if not already present
        new_list.append(num)
        
# Print results
print("Original list : ", lst)
print("Final list after removing duplicates : ", new_list)
   

