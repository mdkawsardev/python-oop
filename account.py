class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print(f"Your balance has been debited {amount},\n Now total balance is: {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"Your balance has been credited {amount},\n Now total balance is: {self.balance}")
    # def total(self):
    #     return self.balance

customer1 = Account(10000, 2323)
customer1.debit(1000)
customer1.credit(20000)
customer1.debit(12000)
