class Person:
    possition = "Python develoer"
    vacancy = 10
    def announce(self):
        print(f"The possition is {self.possition}, and vacancy is {self.vacancy}")

publish = Person()
publish.announce()