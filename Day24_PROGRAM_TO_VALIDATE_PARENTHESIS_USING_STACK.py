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

expression = input("Enter expression : ")           # Input expression string

stack = []                                          # create empty stack

pairs = { '(' : ')' , '{' : '}' , '[' : ']'}        # Define matching pairs

for ch in expression :
    if ch in "({[":                                 # If opening bracket → push
        stack.append(ch)

    elif ch in ")}]":                               # If closing bracket


        if len(stack) == 0:                         # Check if stack is empty
            print("Invalid Parenthesis")
            break

        top = stack.pop()                           # Check matching
        if pairs[ch] != top:
            print("Invalid Parenthesis")
            break


else:                                               #  Check final condition
    if len(stack) == 0:
        print("Valid Parenthesis")
    else:
        print("Invalid Parenthesis")
