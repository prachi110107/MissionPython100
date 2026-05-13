'''
Day42:- Product Of Array Except Itself
Difficulty:- Hard
Concept:- Sliding Window , Hash Map , Dictionary , Frequency Counting
Step 1 : Use two pointers (left and right) to create a sliding window.
Step 2 :  Store frequency of characters in a dictionary.
Step 3 :  Find : window size - maximum frequency character
Step 4 :  If replacements needed become greater than k, shrink the window from the left side.
Step 5 :  Continuously update the maximum valid window length.

'''