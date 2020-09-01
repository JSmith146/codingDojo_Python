from bankaccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.account.balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        print(self.name,"transferred",amount,"to",other_user.name)
        return self


mike = User("Michael","Michael@gmail.com")
john = User("John","John@gmail.com")
susan = User("Susan", "susan@gmail.com")

mike.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(50).display_user_balance()

john.make_deposit(150).make_deposit(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

susan.make_deposit(500).make_withdrawal(25).make_withdrawal(40).make_withdrawal(35).display_user_balance()

john.transfer_money(susan,100).display_user_balance()
susan.display_user_balance()

