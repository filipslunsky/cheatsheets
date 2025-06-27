# LISTS

# fruit_list = ["apple", "pear", "kiwi"]
# num_list = [1, 3, 45, 18]
# tf_list = [True, True, False]
# empty_list = []
# mixed_list = [True, 45, "shoes", 6.9]
# higher_list = [[1, 2, 3], [True, False], "apple", "orange", [10]]

# # print(fruit_list)
# # print(num_list)
# # print(tf_list)
# # print(mixed_list)
# # print(higher_list)

# # print(fruit_list[0])
# # print(fruit_list[-3])
# # print(len(fruit_list))

# # print(fruit_list[len(fruit_list) -1])

# for item in mixed_list:
#     print(item)

# for item in higher_list:
#     for sub_item in item:
#         print(sub_item)

# fruit_list[1] = "mango"

# print(fruit_list)

# fruit_list.insert(2, "cherry")
# print(fruit_list)

# ascending_list = []
# for item in range(1, 51):
#     ascending_list.append(item)

# print(ascending_list)

# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# def get_fibonacci(length):
#     if type(length) != int:
#         print("not integer")
#         return []
#     if length <= 0:
#         print("negative number")
#         return []
#     if length == 1:
#         return [1]
    
#     fibonacci_list = [1, 1]
#     for index in range(0, length - 2):
#         fibonacci_list.append(fibonacci_list[index] + fibonacci_list[index + 1])
#     return fibonacci_list



# fruit_list = ["apple", "pear", "kiwi", "pear", "kiwi", "pear", "kiwi", "pear", "kiwi", "pear", "kiwi", "pear", "kiwi", "pear"]
# # print(fruit_list)
# # while "pear" in fruit_list:
# #     fruit_list.remove("pear")
# # print(fruit_list)

# print(fruit_list)
# fruit_set = set(fruit_list)

# print(fruit_set)

# fruit_set.discard("mango")
# print(fruit_set)

# def get_recatangle_values(a, b):
#     area = a * b
#     circfrnce = 2 * (a + b)
#     return {"area": area, "circumference": circfrnce}



# print(type(get_recatangle_values(3, 4)))
# print(get_recatangle_values(3, 4))

# # rectangle_tuple = get_recatangle_values(3, 4)

# # def describe_rectangle(info_tuple):
# #     # area = info_tuple[0]
# #     # circfrnce = info_tuple[1]
# #     abc, xyz = info_tuple

# #     print(f"Area: {abc}, corcumference: {xyz}")

# # describe_rectangle(rectangle_tuple)

# user_dict = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 56,
#     "address": {
#         "street": "Elm st.",
#         "number": 57,
#         "city": "London"
#     },
#     "scores": [34, 12, 89, 124]
# }

# print(user_dict)
# print(user_dict["age"])

# print(user_dict["address"]["street"])
# print(user_dict["scores"][2])

# for key, value in user_dict.items():
#     print(value)

# print(user_dict.values())

def count_letters(word):
    if type(word) != str:
        print("Not a tring, try again.")
        return {"a": 0}
    
    result_dict = {}
    for letter in word:
        if letter in result_dict.keys():
            result_dict[letter] += 1
        else:
            result_dict[letter] = 1
    
    return result_dict

print(count_letters("hello"))
    
