value = input("Enter a number or string: ")
if value.isdigit(): 
    n = int(value)
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        print("It is a Palindrome Number")
    else:
        print("It is NOT a Palindrome Number")

else:
    # For string
    original = value
    reverse = ""

    # Reverse string using loop
    for ch in original:
        reverse = ch + reverse

    # Check palindrome
    if original == reverse:
        print("It is a Palindrome String")
    else:
        print("It is NOT a Palindrome String")