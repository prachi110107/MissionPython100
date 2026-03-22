'''
Day22:- Implementing stack using list
Difficulty:- Medium
Concept:- Stack = LIFO (Last In First Out)
The last element inserted is the first one to be removed
Basic Operations:
Push → Add element
Pop → Remove last element
Peek → View top element
Display → Show stack
Approach
Step 1 : Create an empty list (stack)
Step 2 : Use append() for push
Step 3 : Use pop() for pop
Step 4 : Use [-1] for peek
Step 5 : Use loop for menu-driven program

'''

# Create empty stack (list)
stack = []

# Run infinite loop for menu
while True:
    print("Stack Operations") 
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    # Step 3: Take user choice
    choice = int(input("Enter your choice : "))

    if choice == 1:
        element = int(input("Enter element to push : "))
        stack.append(element)                                 # add element to stack
        print("Element pushed")                               # push operation

   
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            removed = stack.pop()                              # remove last element
            print("Popped element : ", removed)                # pop operation


    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element : ", stack[-1])                  # last element , peek operation


   
    elif choice == 4:
        print("Stack : ", stack)                                # display operation


    elif choice == 5:
        print("Exiting program")                                 # exit operation
        break

    else:
        print("Invalid choice")