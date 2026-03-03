value = input("enter a number or string : ")
if value.isdigit():

    n = int(value)
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10     
        reverse = reverse * 10 + digit
        n = n // 10   

    if original == reverse :
        print("number of string is a palindrome")
    else:
        print("number or string is not a palindrome")

else:
    original = value
    reverse = "" 
    for ch in original:
        reverse = ch + reverse
    if original == reverse:
        print("It is a Palindrome String")
    else:
        print("It is NOT a Palindrome String")