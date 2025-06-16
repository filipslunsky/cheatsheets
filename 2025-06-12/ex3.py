# LOOPS

# # infinite loop
# while 5 == 5:
#     print("SPAM")


while 5 == 6:
    print("SPAM")


# # infinite loop
# while 5 == 5:
#     print("SPAM")
#     print("SPAM")
#     print("SPAM")
#     break

# print("That was weird...")

# user_input = input("Něco napiš: ")
# print(f"Tvoje odpověď: {user_input}")


# user_input = input("Jak se máš? ")

# while user_input != "konec":
#     user_input = input("Jak se máš? ")

# print("Díky za hru.")

# while True:
#     user_input = input("Jak se máš? ")
#     if user_input == "konec":
#         print("Díky za hru.")
#         break

# while True:
#     user_input = input("zadej číslo mezi 1 a 10: ")
#     user_input_num = int(user_input)
#     if user_input_num >= 1 and user_input_num <= 10:
#         print("cool")
#         break
#     else:
#         print("mezi 1 a 10!!!")

# counter = 0
# while counter < 5:
#     print(counter)
#     # counter =  counter + 1
#     counter += 1

# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1
#     if counter < 1:
#         print("start")

# for counter in range(-5, 0):
#     print(-counter)

for counter in range(1, 6):
    print((counter * 2) -1)
