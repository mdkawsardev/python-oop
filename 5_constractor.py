class Person:
    possition = "Python develoer"
    vacancy = 10
    def __init__(self, name, age): # dunder method which is called automatically. This is a constractor
        self.name = name
        self.age = age
        print(f"Name is: {self.name}\n age is: {self.age}\n possition is: {self.possition}\n vacancy is: {self.vacancy}")


publish = Person("kawsar", 22)
# print(publish.name, publish.age, publish.possition, publish.vacancy)