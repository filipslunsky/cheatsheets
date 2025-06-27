# # CLASSES

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def __repr__(self):
#         return f"Person object, name: {self.first_name} {self.last_name}"

#     def greet(self):
#         return f"Hello, I am {self.first_name}."

# # user = Person("John", "Doe")

# # print(user.greet())
# # print(user.first_name)
# # print(user.last_name)

# # user2 = Person("Jane", "Roe")
# # print(user2.greet())

# # print(user)
# # print(user2)

# book_list = [
#     {
#         "author": "Steven King",
#         "title": "It",
#         "published": 1971    
#     },{
#         "author": "Steven King",
#         "title": "Doctor Sleep",
#         "published": 1980    
#     },{
#         "author": "Steven King",
#         "title": "The Shining",
#         "published": 1975    
#     },{
#         "author": "Lewis Carrol",
#         "title": "Alice's Adventures in Wonderlanf",
#         "published": 1990    
#     }
# ]

# class Book:
#     def __init__(self, author, title, published):
#         self.author = author
#         self.title = title
#         self.published = published
#         self.available = True

#     def change_available(self):
#         self.available = not self.available

# book_objects = []
# for book in book_list:
#     book_obj = Book(book["author"], book["title"], book["published"])
#     book_objects.append(book_obj)


# class Library:
#     def __init__(self, books):
#         self.books = books

#     def lend_book(self, title):
#         found_book = []
#         for book in self.books:
#             if book.title == title:
#                 found_book.append(book)
#                 break
#         if len(found_book) == 0:
#             print("We don't have it")
#         elif found_book[0].available:
#             print("Here you go.")
#             found_book[0].change_available()
#         else:
#             print("Come back later.")

            
        


#     def accept_book(self, title):
#         pass

# my_library = Library(book_objects)

# my_library.lend_book("The Shining")
# my_library.lend_book("The Shining")
# my_library.lend_book("The Shininghhjakhsjkd")
# my_library.lend_book("It")


class Person:
    def __init__(self, name, weight, height):
        self._name = name
        self.weight = weight
        self.height = height
        self.number_fingers = 10
    
    @property
    def get_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi
    
    @property
    def name(self):
        return self._name

person1 = Person("Joe", 89, 1.85)
print(person1.height)
person1.weight = 67
print(person1.get_bmi)
person1.name = "Jim"
print(person1.name)

