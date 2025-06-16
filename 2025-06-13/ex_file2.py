# operátory

# print(10 / 3) # 3.3333333
# print(10 // 3) # 3
# print(10 % 3) # 1
# print(3 ** 2) # 9
# print(3 ** (1/2)) # 1.7320 (odmocnina)

CISLO_PI = 3.14

strana_a = 13
strana_b = 26
plocha = strana_a * strana_b

# print(f"Plocha je: {plocha} cm^2.")

# # logické operátory
# print("ahoj" == "ahoj") # True
# print("ahoj" != "ahoj") # False
# print("ahoj" != "AHOJ") # True

# print(5 > 1) # True
# print(not True) # False
# print(True and False) # False
# print(True or False) # True

# user_password = "12345"
# user_entry = input("Heslo? ")

# if user_entry == user_password:
#     print("You live.")
# elif user_entry == "nevim":
#     print("That is sad.")
# elif user_entry == 123:
#     print("Nope.")
# else:
#     print("You die.")

user_inp = input("Dej mi číslo: ")
user_inp_int = int(user_inp)

if user_inp_int % 2 == 0:
    print("číslo je sudé")
    if user_inp_int > 50:
        print("jakože hodně")
else:
    print("číslo je liché")