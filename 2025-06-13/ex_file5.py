# # Lists

# fruit_list = ["apple", "banana", "kiwi"]
# number_list = [1, 3, 1, 4, 6, 8]
# jumbled_list = [True, False, 56, 7.8, "blablabla", "124"]

# # # print(fruit_list)
# # # print(number_list)
# # # print(jumbled_list)

# # # print(len(fruit_list))
# # # print(len(number_list))
# # # print(len(jumbled_list))

# # # print(max(number_list))


# # # print(fruit_list[1])

# # fruit_list[1] = "mango"
# # # print(fruit_list)

# # marek_list = [["A", "B", "C"], ["yes", "no", "maybe"], [True, False, 5]]
# # # print(marek_list[1][2])

# # for sublist in marek_list:
# #     print(sublist)
# #     for item in sublist:
# #         print(item)

# # for fruit in fruit_list:
# #     print(fruit)

# # def get_every_even_index(my_list):
# #     filtered_list = []
# #     for index in range(0, len(my_list)):
# #         if index % 2 == 0:
# #             filtered_list.append(my_list[index])
# #     print(filtered_list)
# #     return filtered_list

# # get_every_even_index(jumbled_list)


# fruit_set = {"apple", "banana", "kiwi", "apple"}

# print(fruit_set)

# fruit_set.remove("mango")
# print(fruit_set)

# dictionaries
user_dictionary = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 67,
    "address": {
        "street": "Elm St.",
        "number": 90210,
        "city": "Chicago"
    },
    "hobbies": ["fishing", "reading"]
}

# print(user_dictionary)
# print(user_dictionary["last_name"])
# user_dictionary["last_name"] = "Krueger"
# print(user_dictionary["last_name"])
# user_dictionary["eye_color"] = "green"
# print(user_dictionary)

user_address = user_dictionary["address"]
print(user_address["city"])

user_hobbies = user_dictionary["hobbies"]
print(user_hobbies[1])

print(f"the hobby: {user_dictionary['hobbies'][1]}, the city: {user_dictionary["address"]["city"]}")