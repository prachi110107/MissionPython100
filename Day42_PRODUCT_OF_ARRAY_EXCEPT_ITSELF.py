'''
Day42:- Product Of Array Except Itself
Difficulty:- Hard
Concept:- Arrays / Lists , Nested Loop , Multiplication Logic
✅ Approach

1️⃣ Take array elements as input from the user.

2️⃣ Traverse each index of the array.

3️⃣ For every element, multiply all other elements except itself.

4️⃣ Store the product in a new list.

5️⃣ Print the final result list.
Step 1 : Use two pointers (left and right) to create a sliding window.
Step 2 :  Store frequency of characters in a dictionary.
Step 3 :  Find : window size - maximum frequency character
Step 4 :  If replacements needed become greater than k, shrink the window from the left side.
Step 5 :  Continuously update the maximum valid window length.

'''