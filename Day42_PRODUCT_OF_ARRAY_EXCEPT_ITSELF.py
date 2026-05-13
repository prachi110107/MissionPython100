'''
Day42:- Product Of Array Except Itself
Difficulty:- Hard
Concept:- Arrays / Lists , Nested Loop , Multiplication Logic
Approach:
Step 1 : Take array elements as input from the user.
Step 2 : Traverse each index of the array.
Step 3 : For every element, multiply all other elements except itself.
Step 4 : Store the product in a new list.
Step 5 : Print the final result list.

'''

# Product of Array Except Itself

numbers = input("Enter numbers separated by space: ")

# convert into integer list
numbers = [int(i) for i in numbers.split()]

result = []

for i in range(len(numbers)):

    product = 1

    for j in range(len(numbers)):

        if i != j:
            product = product * numbers[j]

    result.append(product)

print("Product array except itself is:")
print(result)