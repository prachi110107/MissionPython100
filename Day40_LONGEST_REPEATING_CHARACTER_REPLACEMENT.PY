'''
Day40:- Longest Repeating Character Replacement
Difficulty:- Hard
Concept:- Sliding Window , Hash Map , Dictionary , Frequency Counting
Approach:
Step 1 : Use two pointers (left and right) to create a sliding window.
Step 2 :  Store frequency of characters in a dictionary.
Step 3 :  Find : window size - maximum frequency character
Step 4 :  If replacements needed become greater than k, shrink the window from the left side.
Step 5 :  Continuously update the maximum valid window length.

'''

s = input("Enter string : ")
k = int(input("Enter value of k : "))

max_length = 0

for i in range(len(s)):

    count = {}
    max_freq = 0

    for j in range(i, len(s)):

        ch = s[j]

        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

        if count[ch] > max_freq:
            max_freq = count[ch]

        length = j - i + 1

       
        replace = length - max_freq                 # characters to replace

        if replace <= k:
            if length > max_length:
                max_length = length

print("Longest repeating character length is :", max_length)