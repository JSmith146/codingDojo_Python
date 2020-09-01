class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(self.name,"transferred",amount,"to",other_user.name)


mike = User("Michael","Michael@gmail.com")
john = User("John","John@gmail.com")
susan = User("Susan", "susan@gmail.com")
mike.make_deposit(100)
mike.make_deposit(200)
mike.make_deposit(50)
mike.make_withdrawal(50)
mike.display_user_balance()

john.make_deposit(150)
john.make_deposit(50)
john.make_withdrawal(50)
john.make_withdrawal(50)
john.display_user_balance()

susan.make_deposit(500)
susan.make_withdrawal(25)
susan.make_withdrawal(40)
susan.make_withdrawal(35)
susan.display_user_balance()

john.display_user_balance()
susan.display_user_balance()
john.transfer_money("susan",100)
john.display_user_balance()
susan.display_user_balance()

