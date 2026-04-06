'''
Day37:- To find first non repeating character in string
Difficulty:- Medium
Concept:- The first character that appears only once
Count frequency of each character
Traverse again → find first with count = 1
Approach:
Step 1 : Take string input
Step 2 : Create dictionary to store frequency
Step 3 : Traverse string → count characters
Step 4 : Traverse again → find first char with count = 1
Step 5 : Print result

'''

# Take input from user
str = input("Enter a string : ")

# Create empty dictionary
char_count = {}

# Count frequency of each character
for ch in str :
    if ch in char_count :
        char_count[ch] += 1
    else :
        char_count[ch] = 1

# Find first non-repeating character
for ch in str :
    if char_count[ch] == 1 :
        print("First non-repeating character is : ", ch)
        break
else:
    print("No non-repeating character found")