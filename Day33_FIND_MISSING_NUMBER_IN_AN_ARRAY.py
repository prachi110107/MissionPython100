'''
Day33:- Find missing number in an array
Difficulty:- Medium
Concept:- Array contains numbers from 1 to n , One number is missing , We need to find that missing number
Approach:
Step 1 : Find expected sum using formula
Step 2 : Find actual sum of array
Step 3 : Missing number = expected - actual

'''


# Ask user to give input
arr = list(map(int, input("Enter elements separated by space : ").split()))

n = len(arr) + 1                                        # finding n

expected_sum = n * (n + 1) // 2                         # Calculating expected sum

actual_sum = sum(arr)                                   # Calculating actual sum

missing = expected_sum - actual_sum                     # Finding missing number

print("Missing number is : ", missing)                  # Print result