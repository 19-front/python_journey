from ast import Return
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("    === Automated Teller Machine ===    ")
while True:
    name = input("Enter name to register: ")
    if 4 <= len(name) <= 10:
        break
    else:
        print("Error: Name must be 4-10 characters. Please try again.")
while True:
    pin = str(input("Enter Pin: "))
    if len(pin) == 4:
        balance = 0
        print(name, "has been registered with a starting balance of $" + str(balance))
        break
    else:
        print("Error: PIN must be 4 characters. Please try again.")

while True:
    print("    === Automated Teller Machine ===    ")
    print("LOGIN")
    name_to_check = input("Enter Name: ")
    pin_to_check = str(input("Enter PIN: "))
    if name == name_to_check and pin == pin_to_check:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials!")
        break

while True:
    atm_menu(name)
    option = input("Chose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    else:
        option == "4"
        account.logout(name)
        break

# ###
# we will add this later
# while True:
    # try:
        # amount = int(input("Enter amount to withdraw: "))
        # if amount <= 0:
            # print("Enter a positive amount.")
        # elif amount > balance:
            # print("Insufficient funds.")
        # else:
            # balance -= amount
            # break
    # except ValueError:
        # print("Please enter a valid number.")
