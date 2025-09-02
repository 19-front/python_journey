def show_balance(balance):
    print("Current balance is $" + str(balance) + ".")

def deposit(balance):
    amount = int(input("Enter an amount to deposite: "))
    balance += amount
    show_balance(balance)
    return balance

def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Error: Insuficient funds.")
    else:
        balance -= amount
        show_balance(balance)
    return balance


def logout(name):
    print("Goodbye", name + "!")
