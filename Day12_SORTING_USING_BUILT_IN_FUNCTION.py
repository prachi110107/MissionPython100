'''Day14:- Matrix addition
Difficulty:- Easy 
Concept:- 2D Lists , Nested loops
Approach:
Step 1 : '''

n=int(input("Enter the no of elements : "))

numbers=[]
for i in range(n):
    num=int(input("Enter the elements : "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Sorted list : " , numbers)