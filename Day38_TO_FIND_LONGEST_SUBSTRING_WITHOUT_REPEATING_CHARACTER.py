'''
Day38:- To find longest substring without repeating character 
Difficulty:- Medium
Concept:- Longest substring with all unique characters
Approach:
Step 1 : Take string input
Step 2 : Use a set to store characters
Step 3 : Initialize:
left = 0
max_length = 0
Step 4 : Traverse with right pointer
Step 5 : If duplicate found:
remove characters from left
Step 6 : Update max length
Step 7 : Print result

'''

# Take input from user
str = input("Enter a string : ")

# Initialize variables
char_set = set()      # stores unique characters
left = 0              # left pointer
max_length = 0        # result

# Traverse using right pointer
for right in range(len(str)):
    
    # If duplicate found
    while str[right] in char_set:
        char_set.remove(str[left])   # remove from left
        left += 1                     # move left pointer
    
    # Add current character
    char_set.add(str[right])
    
    # Update max length
    max_length = max(max_length, right - left + 1)

# Print result
print("Length of longest substring:", max_length)