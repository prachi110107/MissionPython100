'''Program to find the second largest number fromn a list'''

n=int(input("Enter number of elements : "))

numbers=[]
for i in range(n):
    num=int(input("Enter elements : "))
    numbers.append(num)
numbers.sort()

print("Second largest number is : " , numbers[-2])
