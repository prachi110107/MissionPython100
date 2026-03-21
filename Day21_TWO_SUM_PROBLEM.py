'''
Day21:- Two sum problem
Difficulty:- Medium
Concept:- Lists , Loops , Indexing , Condition checking
Approach:
Step 1 : Pick first number
Step 2 : Compare with all next numbers
Step 3 : If sum matches → print indices

'''
# Create a list of numbers
nums = [11 , 5 , 25 , 28]
# define target
target = 35

found = False                                     # Declare the flag variable to check if pair found 

for i in range(len(nums)):                        # Outer loop → picks first element one by one
    for j in range(i+1 , len(nums)):              # Inner loop → picks second element after i , also avoids repeating pairs
        if nums[i] + nums[j] == target :          # Check if sum of two elements equals target
            print("indices" , i , j)              # If condition satisfied , print indices
            found = true                          # If satisfied , print indices

# After loop, check if no pair was found
if not found:
    print("No two numbers found whose sum is equal to target")