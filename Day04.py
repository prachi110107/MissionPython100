n = int(input("Enter a number : "))
original = n
digits = len(str(n))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10
if total == original:
    print("It is an Armstrong Number")
else:
    print("It is NOT an Armstrong Number")