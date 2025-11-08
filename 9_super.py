class Person:
    name = "imran"
    def __init__(self):
        print("Good Morning")

class Salary(Person):
    salary = 12000
    def __init__(self):
        super().__init__() # This super mathod allows to print Person's constructor. Without his method it will raise an error
        print(f"Salary is {self.salary}")


a = Salary()


