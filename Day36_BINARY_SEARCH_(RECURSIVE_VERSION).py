'''
Day36:- Binary search (Recursive version)
Difficulty:- Medium
Concept:-  Binary Search works only on sorted array
Idea:Divide array into two halves , Compare middle element with target , Search in left OR right half
mid = (low + high) // 2
If target == mid → found 
If target < mid → search left
If target > mid → search right
Approach:
Step 1 : Take sorted array input
Step 2 : Take target value
Step 3 : Define recursive function with:
low index
high index
Step 4 : Base case:
if low > high → not found
Step 5 : Find mid
Step 6 : Compare and call recursively
Step 7 : Print result

'''

# Define recursive function
def binary_search(arr, low, high, target) :
    
    # Base case 
    if low > high :
        return -1
    
    # Find middle index
    mid = (low + high) // 2
    
    # Check if middle element is target
    if arr[mid] == target :
        return mid
    
    # If target is smaller → search left
    elif target < arr[mid] :
        return binary_search(arr, low, mid - 1, target)
    
    # If target is larger → search right
    else :
        return binary_search(arr, mid + 1, high, target)


# Take input from user
arr = list(map(int, input("Enter sorted elements : ").split()))
target = int(input("Enter element to search : "))

# Call function
result = binary_search(arr, 0, len(arr) - 1, target)

# Print result
if result != -1 :
    print("Element found at index : ", result)
else :
    print("Element not found")