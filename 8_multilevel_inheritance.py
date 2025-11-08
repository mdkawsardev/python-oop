# multilevel inheritance of one class to another class
class Employee:
    company = "Mircrosoft"
    def show(self):
        print(f"The company name is: {self.company}")


class Person(Employee): # This is called multilevel inheritance. A class inside of another class
    name = "Kawsar"
    def prin(self):
        print(f"{self.name} works at {self.company}")

class Salary(Person): # This is called multilevel inheritance.
    salary = 12000
    def mySalary(self):
        print(f"{self.name} works at {self.company}, and his salary is: {self.salary}")

a = Salary()
a.show()
a.name = "Imran" # This is called instance attribute
a.prin()
a.mySalary()