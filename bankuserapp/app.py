
# the code
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
    def change_name(self, new_name):
        self.name = new_name
    def change_pin(self, new_pin):
        self.pin = new_pin
    def change_password(self, new_password):
        self.password = new_password
    
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    def change_bankuser_name(self, bankuser_new_name):
        self.name = bankuser_new_name
    def change_bankuser_pin(self, bankuser_new_pin):
        self.pin = bankuser_new_pin
    def change_bankuser_password(self, bankuser_new_password):
        self.password = bankuser_new_password
    def show_balance(self):
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount

    # transfer logic
    def transfer_money(self, recipient, amount, pin):
        if self.pin == pin:
            self.withdraw(amount)
            recipient.deposit(amount)
            return True
        return False
    
    # request logic
    def request_money(self, sender, amount, pin, password):
        if self.pin == pin and sender.password == password:
            sender.withdraw(amount)
            self.deposit(amount)
            return True
        return False
