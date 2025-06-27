# LOOPS

# WHILE LOOPS
# while True:
#     print("SPAM")


# while True:
#     print("SPAM")
#     break


# counter = 0

# while counter < 10:
#     # print("going...")
#     print(counter)
#     # counter = counter + 1
#     counter += 1


# user_input = input("Enter number: ")
# print(user_input)


# password = "ahoj"

# while True:
#     user_input = input("Enter password: ")
#     if user_input == password:
#         print("Access granted")
#         break
#     else:
#         print("Access denied.")

# while input("Enter password: ") != password:
#     print("denied")

# print("granted")


# FOR LOOPS
my_phrase = "Hello World"

# for letter in my_phrase:
#     print(letter)

# for number in range(0, 5):
#     print(number)

# print(my_phrase[3])

# print(len(my_phrase))

# for index_num in range(0, len(my_phrase), 2):
#     # if index_num % 2 == 0:
#     #     print(my_phrase[index_num])
#     print(my_phrase[index_num])


while True:
    user_input = input("What is the number? ")
    if user_input.isnumeric():
        user_input_int = int(user_input)
        if user_input_int % 2 == 0 and user_input_int % 3 == 0:
            print("Both 2 and 3.")
        elif user_input_int % 2 == 0:
            print("Just 2.")
        elif user_input_int % 3 == 0:
            print("Just 3.")
        else:
            print("Neither.")
        break
    else:
        print("Not a number!!!")
    