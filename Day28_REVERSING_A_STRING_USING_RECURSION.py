'''
Day28 :- Program to reverse a string using recursion 
Difficulty :- Medium
Concepts :- 
Recursion = function calling itself
To reverse a string: Take first character , Move it to the end , Repeat for remaining string
reverse("abc") = reverse("bc") + "a"
Approach 
Step 1 : Take string input
Step 2 : Define recursive function
Step 3 : Base case → if string is empty → return string
Step 4 : Recursive case → reverse remaining string + first character
Step 5 : Print result

'''


string = input("Enter a string : ")              # Take input from user

def reverse_string(str):                         # Define recursive function
    
    if len(str) <= 1:                            # Base case 
        return str
    
    return reverse_string(str[1:]) + str[0]      # Recursive case 

reverse = reverse_string(string)                 # Call function

print("Reversed string is:", reverse)            # Print result


