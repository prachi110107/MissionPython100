'''
Day45:- Count number of nice subarrays using hashmaps
Difficulty:- Hard
Concept:- Prefix Sum , HashMap / Dictionary , Odd Number Counting
Approach:
Step 1 : Traverse the array and count the number of odd elements seen so far.
Step 2 : Store odd counts in a hashmap with their frequency.
Step 3 : For every element, check:odd_count - k
Step 4 : If it exists in hashmap:a nice subarray is found.Add its frequency to the answer.
Step 5 : Update hashmap with current odd count frequency.

'''
# Count Number of Nice Subarrays

numbers = input("Enter array elements separated by space: ")
numbers = [int(i) for i in numbers.split()]

k = int(input("Enter value of k: "))

count = 0
odd_count = 0

hashmap = {0: 1}

for num in numbers:

    # check odd number
    if num % 2 != 0:
        odd_count += 1

    # check if odd_count - k exists
    if odd_count - k in hashmap:
        count += hashmap[odd_count - k]

    # update hashmap
    if odd_count in hashmap:
        hashmap[odd_count] += 1
    else:
        hashmap[odd_count] = 1

print("Number of nice subarrays is:", count)