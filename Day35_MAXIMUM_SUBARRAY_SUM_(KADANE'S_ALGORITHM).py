'''
Day35:- Maximum subarray sum (Kadane's algorithm)
Difficulty:- Medium
Concept:-  Given an array , Find maximum sum of a contiguous subarray
Approach:
Step 1 : Take input array
Step 2 : Initialize:
max_sum = first element
current_sum = 0
Step 3 : Traverse array:
Add element to current_sum
If current_sum > max_sum → update
If current_sum < 0 → reset to 0
Step 4 : Print max_sum

'''


# Ask user to give input
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Initialize variables
max_sum = arr[0]                      # stores maximum subarray sum
current_sum = 0                       # stores current running sum

for num in arr:                       # Traverse array
    
    current_sum += num                # Add current element
    
    if current_sum > max_sum:         # Update max sum if needed
        max_sum = current_sum
    
    if current_sum < 0:               # Reset current sum if negative
        current_sum = 0

# Print result
print("Maximum Subarray Sum is:", max_sum)      