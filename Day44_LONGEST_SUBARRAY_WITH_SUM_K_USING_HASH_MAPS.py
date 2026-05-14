'''
Day44:- Longest subarray with sum K using hashmaps
Difficulty:- Hard
Concept:- Prefix Sum , HashMap / Dictionary , Array Traversal
Approach:
Step 1 : Traverse the array and keep calculating the prefix sum.
Take array elements as input from the user.
Step 2 : If the prefix sum itself becomes equal to k : update maximum length.
Step 3 : Check whether : prefix_sum - k exists in the hashmap.
Step 4 : If it exists : a subarray with sum k is found.Calculate its length and update maximum length.
Step 5 : Store prefix sum with its first occurrence index in hashmap.

'''

# Longest Subarray With Sum K

numbers = input("Enter array elements separated by space: ")
numbers = [int(i) for i in numbers.split()]

k = int(input("Enter value of k: "))

prefix_sum = 0
max_length = 0

hashmap = {}

for i in range(len(numbers)):

    prefix_sum += numbers[i]

    # if prefix sum itself equals k
    if prefix_sum == k:
        max_length = i + 1

    # check if remaining sum exists
    if prefix_sum - k in hashmap:

        length = i - hashmap[prefix_sum - k]

        if length > max_length:
            max_length = length

    # store first occurrence only
    if prefix_sum not in hashmap:
        hashmap[prefix_sum] = i

print("Longest subarray length is:", max_length)