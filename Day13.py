'''Program to merge two lists'''

n1 = int(input("Enter the number of elements of list1 : "))
list1 = []
for i in range(n1):
    num1 = int(input("Enter the elements : "))
    list1.append(num1)
    
n2 = int(input("Enter the number of elements of list2 : "))
list2 = []
for i in range(n2):
    num2 = int(input("Enter the elements : "))
    list2.append(num2)

merged_list = list1+list2
print("list1 : " , list1)
print("list2 : " , list2)
print("merged_list : " , merged_list)