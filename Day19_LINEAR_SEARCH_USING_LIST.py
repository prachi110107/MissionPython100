'''Program to perform linear search'''
n = int(input("Enter the number of elements : "))
arr = []
print("Enter elements : ")
for i in range(n) :
    num = int(input())
    arr.append(num)

key = int(input("Enter the number which is to be found : "))
found = False

for i in range(n):
    if arr[i] == key:
        print("Element found at position " , i + 1)
        found = True
        break

if not found:
    print("Element not found")   