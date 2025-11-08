class Employee:
    number = 1
    @classmethod
    def show(cls):
        print(f"The class attibute is: {cls.number}") # It will print class attribute not instance attribute
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


a = Employee()
a.name = "Imran Kawsar"
print(a.name)