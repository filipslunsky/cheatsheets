# jumbled_list = ["asghd", 12, 89, 54.1, 21.9, True, False, "kjhjkjkh"]

# def give_me_strings(my_list):
#     string_list = []
#     for item in my_list:
#         if type(item) == str:
#             string_list.append(item)
#     return string_list

# print(give_me_strings(jumbled_list))

# def give_me_strings_fast(my_list):
#     return [item for item in my_list if type(item) == str]

# print(give_me_strings_fast(jumbled_list))

# def give_me_sorted_lists(my_list):
#     stirng_list = [item for item in my_list if type(item) == str]
#     boolean_list = [item for item in my_list if type(item) == bool]

#     return (stirng_list, boolean_list)

# print(give_me_sorted_lists(jumbled_list))


higher_list = [[1, 2, 3], [True, False, True], ["abc", "def", "ghi"]]

# print(higher_list[2][1])

def flatten_list(my_list):
    flattened_list = []
    for sublist in my_list:
        for item in sublist:
            flattened_list.append(item)
    
    return flattened_list


print(flatten_list(higher_list))