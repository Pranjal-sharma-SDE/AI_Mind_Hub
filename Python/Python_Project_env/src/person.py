
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"the {self.name} is {self.age} years old")