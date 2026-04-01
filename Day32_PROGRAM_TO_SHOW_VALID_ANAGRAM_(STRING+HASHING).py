'''
Day32:- Program to show valid anagram (string + hashing)
Difficulty:- Medium
Concept:- Anagram = two strings having : Same characters , Same frequency , Order does NOT matter
Approach:
Step 1 : Take two strings as input
Step 2 : If lengths are different → not anagram
Step 3 : Create empty dictionary
Step 4 : Traverse first string → increase count
Step 5 : Traverse second string → decrease count
Step 6 : If all values become 0 → valid anagram
Step 7 : Else → not anagram

'''
# Ask user to enter two strings
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

if len(str1) != len(str2) :                      # Check length
    print("Not anagram")

else :                                           # Create empty dictionary
    char_count = {}

    for ch in str1 :                             # Loop runs for each character in the string
        if ch in char_count :                    # Check whether character already present in dictionary or not
            char_count[ch] += 1                  # If character already exists , increase its count by 1
        else :                                   # If character is seen first time
            char_count[ch] = 1                   # Add it to dictionary with count 1

    
    for ch in str2 :                            # Loop runs for each character in the string
        if ch in char_count :                   # Check whether character already present in dictionary or not
            char_count[ch] -= 1                 # Reduce count because We found a matching character So we cancel it out
        else :                                  # If character NOT found in dictionary
            print("Not an anagram")             # Second string has different characters
            break                               # Exists loop immediately


    else:                                       
        for value in char_count.values():       # We check all values in dictionary
            if value != 0:                      # Mismatch , Not an anagram
                print("Not an Anagram")         
                break                           # Exists loop
        else:                                   
            print("Valid Anagram")              # All values 0 i.e Perfect match 