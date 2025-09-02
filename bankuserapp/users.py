import homepage
import app

homepage

print()
# using code task 1
user1 = app.User("Titi", 1111, "pass1111")
print(user1.name, user1.pin, user1.password)
print()
# using code task 2
user1.change_name("Alice")
user1.change_pin("1212")
user1.change_password("pass1212")
print(user1.name, user1.pin, user1.password)
print()
# using bankuser code task 3
bankuser = app.BankUser("David", 4433, "433password")
print(bankuser.name, bankuser.pin, bankuser.password)
bankuser.change_bankuser_name("John")
bankuser.change_bankuser_pin(6677)
bankuser.change_bankuser_password("password1212")
print(bankuser.name, bankuser.pin, bankuser.password)
print()
print(f"Balance: ${float(bankuser.show_balance())}")
print()
print(bankuser.name, bankuser.pin, bankuser.password)
print(f"Balance: ${float(bankuser.show_balance())}")
bankuser.deposit(100)
print(f"Balance: ${float(bankuser.show_balance())}")
bankuser.withdraw(50)
print(f"Balance: ${float(bankuser.show_balance())}")
# code for testing task 5
user1 = app.BankUser("Dadi", 1122, "pass1")
user2 = app.BankUser("Vic", 4321, "pass2")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
success = user2.transfer_money(user1, 500, 4321)
if success:
    user2.show_balance()
    user1.show_balance()
    req_success = user2.request_money(user1, 500, 1234, "pass1")
    if req_success:
        user2.show_balance()
        user1.show_balance()
print(user1.name, "balance is: $",float(user1.show_balance()))
print(user2.name, "balance is: $",float(user2.show_balance()))