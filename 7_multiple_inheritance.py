# Multiple inheritance
class Employee:
    company = "Mircrosoft"
    def show(self):
        print(f"The company name is: {self.company}")


class Person: 
    name = "Kawsar"
    def prin(self):
        print("I'm Person class")
        print(f"{self.name} works at {self.company}")

class Salary(Person, Employee): # This is called multiple-inheritance class
    salary = 12000
    def mySalary(self):
        print("Hello I'm")
        print(f"{self.name} works at {self.company}, and his salary is: {self.salary}")

a = Salary()
print(a.salary)
a.mySalary()

print(a.name)
a.prin()

print(a.company)