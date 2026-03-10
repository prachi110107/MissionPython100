'''Program to count number of consonant , vowels , and digits '''

n = str(input("Enter The String:"))
digits = 0
vowels = 0
consonant = 0
for ch in n:
    if ch.isdigit():
        digits += 1
    elif ch.lower() in "aeiou" :
        vowels += 1
    elif ch.isalpha() :
        consonant += 1
    
print("consonants:", consonant)
print("vowels:", vowels)
print("digits:", digits)