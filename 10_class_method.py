class Employee:
    number = 1
    @classmethod
    def show(cls):
        print(f"The class attibute is: {cls.number}") # It will print class attribute not instance attribute


a = Employee()
a.number = 22
a.show()