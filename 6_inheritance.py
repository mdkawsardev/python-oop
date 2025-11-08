class Employee:
    company = "Google"
    def show(self):
        print(f"Company is {self.company}")

class Person(Employee): # This is called inheritance of class. One class inside of another class
    name = "Imran"
    def apply(self):
        print(f"Hello I'm {self.name}, and I works at {self.company}")

a = Person()
print(a.company)
print(a.name)
a.apply()