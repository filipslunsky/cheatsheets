# # List
# fruits = ["apple", "banana", "orange"]
# weird_list = ["apple", 57, "banana", True, False, "orange", -7.1]

# print(fruits)
# print(weird_list)

# print(len(weird_list))

# print(weird_list[2])
# print(weird_list[-1])
# print(weird_list[-2])
# print(weird_list[len(weird_list) - 1])
# fruits[1] = "mango"

# print(fruits)

# weird_list.remove("banana")
# weird_list.pop(1)
# print(weird_list)

def give_me_from_to(bottom, top):
    numbers = []
    for number in range(bottom, top + 1):
        numbers.append(number)
    
    return numbers
    
# numbers_list = give_me_from_to(1, 1000)


def get_fibonacci(total):
    if total < 1:
        return []
    elif total == 1:
        return [1]
    fibonacci = [1, 1]

    for indx in range(0, total - 2):
        fibo = fibonacci[indx] + fibonacci[indx + 1]
        fibonacci.append(fibo)

    return fibonacci

print(get_fibonacci(2))

# my_list = [1, 2, 3, 2, 1, 4, 5]
# my_set = {1, 2, 3, 2, 1, 4, 5}

# print(my_list[2])
# print(my_set)

# for item in my_set:
#     print(item)

# my_tuple = (1, 2, 3)
# print(len(my_tuple))
# print(my_tuple)
# print(my_tuple[1])

# my_list_from_tuple = list(my_tuple)

# my_list_from_tuple[1] = 5
# print(my_list_from_tuple)
# tuple(my_list_from_tuple)