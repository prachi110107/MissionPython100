'''
Day09:- To count digits , vowels and consonants
Difficulty:- Easy 
Concept:- Strings
• Loop (for)
• Conditional statements (if-elif)
• String functions:

isdigit()
isalpha()
lower()
Approach:
Step 1 : Take a string input from the user
Initialize counters for digits, vowels, and consonants
Traverse each character in the string
Check:
If digit → increase digit count
If vowel → increase vowel count
If alphabet but not vowel → consonant
Print the counts

 '''

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