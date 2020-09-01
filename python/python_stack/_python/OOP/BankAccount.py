class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        # self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance-amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print("Balance: $",self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+self.int_rate)
            return self
        else:
            return self


account_1 = BankAccount()
account_2 = BankAccount()

account_1.deposit(50).deposit(100).deposit(50).withdraw(25).yield_interest().display_account_info()
account_2.deposit(200).deposit(300).withdraw(50).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()