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

acc1 = BankAccount(0.03, 1000)
acc2 = BankAccount(0.05, 5000)

acc1.deposit(100).deposit(100).deposit(300).withdraw(300).yield_interest().display_account_info()

acc2.deposit(500).deposit(500).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()

# @classmethod
# def print_acc(cls):
#     print(acc1)