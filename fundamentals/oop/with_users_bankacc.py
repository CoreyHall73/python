class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        # print(self.balance)
        return self



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_balance(self):
        self.account.display_account_info()
        print(self.name)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


Corey = User('Corey', '@me')

Corey.make_deposit(500).display_balance()
Corey.make_withdrawal(250).display_balance()