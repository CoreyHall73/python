class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


Corey = User('Corey', '@me')
Noah = User("noah", "noah@email")
Ben = User("Ben", "Ben@email")

Corey.make_deposit(500).make_deposit(1000).make_deposit(500).make_withdrawal(500.)display_balance()
# Corey.make_deposit(1000)
# Corey.make_deposit(500)
# Corey.make_withdrawal(500)
# Corey.display_balance()

Noah.make_deposit(1000).make_deposit(2000).make_withdrawal(500).make_withdrawal(500).display_balance()
# Noah.make_deposit(2000)
# Noah.make_withdrawal(500)
# Noah.make_withdrawal(500)
# Noah.display_balance()

Ben.make_deposit(10000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).display_balance()
# Ben.make_withdrawal(1000)
# Ben.make_withdrawal(1000)
# Ben.make_withdrawal(1000)
# Ben.display_balance()

Ben.transfer_money(Corey, 5000)
Corey.display_balance()
Ben.display_balance()