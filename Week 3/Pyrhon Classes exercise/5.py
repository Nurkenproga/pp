class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print(self.balance)

    def withdraw(self, money):
        if(money <= self.balance):
            print(f"your money: {money}")
            self.balance = self.balance - money
        else:
            print("You don't have enough balance :(")

    def cash_in(self, money):
        self.balance = self.balance + money

c = input()
a = Account(c, 2000)
a.deposit()
a.withdraw(1500)
a.deposit()
a.cash_in(2500)
a.deposit()
