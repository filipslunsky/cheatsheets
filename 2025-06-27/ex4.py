# CLASSES

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Person object, name: {self.first_name} {self.last_name}"

    def greet(self):
        return f"Hello, I am {self.first_name}."

# user = Person("John", "Doe")

# print(user.greet())
# print(user.first_name)
# print(user.last_name)

# user2 = Person("Jane", "Roe")
# print(user2.greet())

# print(user)
# print(user2)

book_list = [
    {
        "author": "Steven King",
        "title": "It",
        "published": 1971    
    },{
        "author": "Steven King",
        "title": "Doctor Sleep",
        "published": 1980    
    },{
        "author": "Steven King",
        "title": "The Shining",
        "published": 1975    
    },{
        "author": "Lewis Carrol",
        "title": "Alice's Adventures in Wonderlanf",
        "published": 1990    
    }
]