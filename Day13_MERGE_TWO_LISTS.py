'''
Day13:- Merge two list
Difficulty:- Easy 
Concept:- Lists , User input , Loops , append() method , List concatenation
Approach:
Step 1 : Take number of elements for both lists
Step 2 : Take input elements using loops
Step 3 : Store elements in lists
Step 4 : Merge lists using + operator
Step 5 : Print results

'''


# First input list
lst = input("Enter elements separated by space: ").split()

# Convert that input list into integers
lst = [int(x) for x in lst]

# Sort the list 
lst.sort()
# Take number of elements for list1
n1 = int(input("Enter the number of elements of list1 : "))
list1 = []                                          # Create empty list1
for i in range(n1):                                 # Loop runs n1 times
    num1 = int(input("Enter the elements : "))      # take element input
    list1.append(num1)                              # add element to list1

# Take number of elemrnts for list2   
n2 = int(input("Enter the number of elements of list2 : "))
list2 = []                                           # Create empty list2
for i in range(n2):                                  # loop runs n2 times
    num2 = int(input("Enter the elements : "))       # take element input
    list2.append(num2)                               # add element to list2

merged_list = list1+list2                            # Merge both lists                       
# Print all lists
print("list1 : " , list1)
print("list2 : " , list2)      
print("merged_list : " , merged_list)