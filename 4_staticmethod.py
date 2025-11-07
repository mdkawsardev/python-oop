class Person:
    possition = "Python develoer"
    vacancy = 10
    def announce(self):
        print(f"The possition is {self.possition}, and vacancy is {self.vacancy}")

    @staticmethod # That means it doesn't need any attributes of class, It can run anyway
    def greet():
        print("Good Morning")

publish = Person()
publish.announce()
publish.greet()