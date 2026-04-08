'''
Day39:- To find longest character replacement (advanced sliding window)
Difficulty:- Hard
Concept:- Given a string and integer k , You can replace at most k characters , Find longest substring with same characters after replacement
Approach:
Step 1 : Take string and k as input
Step 2 : Use dictionary for frequency
Step 3 : Initialize:
left = 0
max_freq = 0
max_length = 0
Step 4 : Traverse with right pointer
Step 5 : Update frequency and max_freq
Step 6 : If window invalid → shrink from left
Step 7 : Update max_length
Step 8 : Print result

'''

# Take input
str = input("Enter a string : ")
k = int(input("Enter value of k : "))

# Initialize variables
char_count = {}                             # stores frequency
left = 0
max_freq = 0                                # highest frequency in window
max_length = 0

# Traverse using right pointer
for right in range(len(str)) :
    
    # Update frequency
    ch = str[right]
    if ch in char_count :
        char_count[ch] += 1
    else:
        char_count[ch] = 1
    
    # Update max frequency
    max_freq = max(max_freq, char_count[ch])
    
    # Check if window is valid
    if (right - left + 1) - max_freq > k :
        
        # Shrink window
        char_count[str[left]] -= 1
        left += 1
    
    # Update max length
    max_length = max(max_length, right - left + 1)

# Print result
print("Longest substring length : ", max_length)