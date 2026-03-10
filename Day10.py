'''Removing duplicates from a given string or list'''

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
   