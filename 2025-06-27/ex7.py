class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}\nAge: {self.age}"

    def greet(self):
        return f"Hello, I am {self.first_name}."
    

    

person1 = Person("John", "Doe", 53)
print(person1)


class Student(Person):
    def __init__(self, first_name, last_name, age, score, passed):
        super().__init__(first_name, last_name, age)
        self.score = score
        self.passed = passed

    def greet(self):
        return f"Yo, what's up? I am {self.first_name}"

student1 = Student("Jim", "Yoe", 22, 92, True)
print(student1)
print(student1.greet())
print(person1.greet())