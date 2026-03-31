'''
Day31:- To perform two sum problem optimized using dictionary
Difficulty:- Medium
Concept:- Given a list and a target
Find two indices such that:
nums[i] + nums[j] = target
Approach:
Step 1 : Create empty dictionary
Step 2 : Traverse list
Step 3 : For each element:
         Find complement = target - element
Step 4 : If complement exists in dictionary → solution found
Step 5 : Else store element with index
Step 6 : Print indices

'''
# Take input list
num = list(map(int, input("Enter elements separated by space: ").split()))

target = int(input("Enter target value: "))        # Take target value     
                                                     
num_dict = {}                                      # Create empty dictionary
                                                   # will store {value: index}

found = False                                      # Declare the flag variable to check if pair found 

for i in range(len(num)):                          # Outer loop → picks first element one by one
    for j in range(i+1 , len(num)):                # Inner loop → picks second element after i , also avoids repeating pairs
        if num[i] + num[j] == target :             # Check if sum of two elements equals target
            print("indices" , i , j)               # If condition satisfied , print indices
            found = True                           # If satisfied , print indices

# After loop, check if no pair was found
if not found:
    print("No two numbers found whose sum is equal to target")