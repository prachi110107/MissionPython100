'''Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''

n=int(input("Enter number of elements : "))

numbers=[]
for i in range(n):
    num=int(input("Enter elements : "))
    numbers.append(num)
numbers.sort()

print("Second largest number is : " , numbers[-2])
