'''
Day09:- To count digits , vowels and consonants
Difficulty:- Easy 
Concept:- Strings , Loop , Conditional statements , String functions : isdigit() , isalpha() , lower()
Approach:
Step 1 : Take a string input from the user
Step 2 : Initialize counters for digits, vowels, and consonants
Step 3 : Traverse each character in the string
         Check:
         If digit → increase digit count
         If vowel → increase vowel count
         If alphabet but not vowel → consonant
Step 4 : Print the counts

 '''
# Ask user to input the srting
n = str(input("Enter The String:"))

# Initialize counters
digits = 0                                 # counts numbers (0-9)
vowels = 0                                 # counts vowels (a, e, i, o, u)
consonant = 0                              # counts consonants

# Traverse each character in the string
for ch in n:

    if ch.isdigit():                       # Check if character is a digit
        digits += 1                        # increase digit count
   
   
    elif ch.lower() in "aeiou" :           # Check if character is a vowel
        vowels += 1                        # increase vowel count
    
    elif ch.isalpha() :                    # check if character is an alphabet 
        consonant += 1                     # increase consonant count 

# Print results    
print("consonants:", consonant)
print("vowels:", vowels)
print("digits:", digits)