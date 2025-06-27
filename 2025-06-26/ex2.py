# CONDITIONALS

# my_number = 5

# if my_number > 5:
#     print("more than 5")
#     if type(5) == int:
#         print("integer type")
# elif my_number == 5:
#     print("exactly 5")
# else:
#     print("unknown")

tested_num = 14

if type(tested_num) == int:
    if tested_num % 2 == 0:
        print("Is even.")
    else:
        print("Is odd.")
else:
    print("Wrong type.")

