'''
Day43:- Subarray sum equals K
Difficulty:- Hard
Concept:- Prefix Sum , HashMap / Dictionary , Array Traversal
Approach:
Step 1 : Traverse the array and keep calculating the running sum.
Step 2 : Store prefix sums in a dictionary with their frequency.
Step 3 : For every element, check : current_sum - k
Step 4 : If this value exists in the dictionary: a subarray with sum k is found.
Step 5 : Update the count and continue traversal.

'''

# Subarray Sum Equals K

numbers = input("Enter array elements separated by space: ")
numbers = [int(i) for i in numbers.split()]

k = int(input("Enter value of k: "))

count = 0
current_sum = 0

prefix_sum = {0: 1}

for num in numbers:

    current_sum += num

    if current_sum - k in prefix_sum:
        count += prefix_sum[current_sum - k]

    if current_sum in prefix_sum:
        prefix_sum[current_sum] += 1
    else:
        prefix_sum[current_sum] = 1

print("Number of subarrays with sum", k, "is:", count)