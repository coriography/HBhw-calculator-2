"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("Enter your equation, prefix first, or quit.")
    user_input = user_input.split(" ")
    command = user_input.pop(0)

    if command == '+':
        if len(user_input) == 2:
            first_num, second_num = user_input
            first_num = int(first_num)
            second_num = int(second_num)
            print(add(first_num, second_num))
        else:
            print("Please enter correct input.")
# Replace this with your code
# given user input, turn input into list using split
# pop off first item and assign to variable command
# our user input is now numbers
# we need to change those into integers
# we to assign those integers to variables 
    # AN IDEA
    # count = 0
    # for int in int_list
        # int{count} = int
        # count += 1

# pass those integers into the function that matches our command

# if the first item in the list is "+"
    # check if length of list is 2
        #if yes
            #turn 2nd and 3rd items to integers
            #call add function with integers

        #if no
            #error (make them input again)


# if the first item in the list is "-"