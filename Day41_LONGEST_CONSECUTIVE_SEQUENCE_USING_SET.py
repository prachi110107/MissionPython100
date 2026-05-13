'''
Day41:- Longest Consecutive Sequence Using Set
Difficulty:- Hard
Concept:- Set Data Structure , Hashing , Sequence Traversal
Step 1 : Store all numbers in a set for fast searching.
Step 2 : Traverse each number in the set.
Step 3 : Check if the number is the starting point of a sequence : num - 1 not in set
Step 4 : Use a loop to count consecutive numbers : num + 1, num + 2, ...
Step 5 : Update the maximum sequence length.

'''

# Longest Consecutive Sequence using Set
numbers = input("Enter numbers separated by space: ")

# convert into integer list
numbers = [int(i) for i in numbers.split()]

# convert list into set
num_set = set(numbers)
longest = 0

for num in num_set:

    # check starting point
    if num - 1 not in num_set:

        current = num
        length = 1

        # check consecutive numbers
        while current + 1 in num_set:
            current += 1
            length += 1

        # update longest length
        if length > longest:
            longest = length

print("Longest consecutive sequence length is:", longest)