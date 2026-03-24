'''
Day24:- Program to validate parenthesis using stack 
Difficulty:- Medium
Concept:- We use Stack (LIFO) to check balanced parentheses
Rules: Opening brackets → ( { [ → push into stack
       Closing brackets → ) } ] → check and pop
Approach
Step 1 : Create empty stack
Step 2 : Traverse string
Step 3 : If opening bracket → push
Step 4 : If closing bracket:
         Check stack not empty
         Check top matches
         Pop
Step 5 : After loop:
         If stack empty → valid
         Else → invalid

'''

# Take input string
expression = input("Enter expression: ")

# Create empty stack
stack = []

# Define matching pairs
pairs = {')': '(', '}': '{', ']': '['}

# Traverse each character
for ch in expression:

    # If opening bracket → push
    if ch in "({[":
        stack.append(ch)

    # If closing bracket
    elif ch in ")}]":

        # Check if stack is empty
        if len(stack) == 0:
            print("Invalid Parenthesis")
            break

        # Check matching
        top = stack.pop()
        if pairs[ch] != top:
            print("Invalid Parenthesis")
            break

# Check final condition
else:
    if len(stack) == 0:
        print("Valid Parenthesis")
    else:
        print("Invalid Parenthesis")


