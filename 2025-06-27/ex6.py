from ex5 import chroustator as ch

# print(ch.multiply(6, 7))
# print(ch.add(6, 7))

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    @classmethod
    def initiate_from_string(cls, book_string):
        title, pages = book_string.split(",")
        return cls(title, pages)

book1 = Book("Harry Potter", 809)
print(book1.title)

book2 = Book.initiate_from_string("Alice,621")
print(book2.title)
