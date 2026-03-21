'''
Day10:- Remove duplicates from list
Difficulty:- Medium
Concept:- Strings , Lists , Loops , Membership checking , Building new result
Approach:
For String:
Step 1 : Take input string
Step 2 : Traverse each character
Step 3 : Add only if not already present
Step 4 : Build new string
For List:
Step 1 : Take number of elements
Step 2 : Store elements in list
Step 3 : Traverse list
Step 4 : Add only unique elements to new list

'''

'''For string'''
S=input("Enter a string : ")
result = ""
for ch in S :
    if ch not in result :
        result = result + ch
print("Initial string : ", S)
print("Final string after removing duplicates : ", result)

'''For list'''
N=int(input("Enter number of elements : "))
numbers = ""
for i in range(N):
    num = int(input("Enter elements : "))
    numbers.append(num)
new_list = ""
for num in numbers :
    if num not in new_list:
        new_list.append(num)
print("Original list : ", N)
print("Final list after removing duplicates : ", new_list)
   