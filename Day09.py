# Input from user
text = input("Enter a string: ")

digits = 0
vowels = 0
consonants = 0

i = 0

while i < len(text):
    ch = text[i]

    if ch.isdigit():
        digits += 1

    elif ch.lower() in 'aeiou':
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    i += 1

# Output
print("Digits:", digits)
print("Vowels:", vowels)
print("Consonants:", consonants)
