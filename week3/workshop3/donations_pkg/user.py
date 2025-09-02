#login function
def login(database, username, password):
    if username in database and database[username]==password:
        print(f"\nWelcome, {username}")
        return username
    elif username in database and database[username]!=password:
        print(f"\nOops {username}, password is invalid \n\n Try again")
        return ""
    else:
        print(f"\nLogin credentials not valid")
        return ""

#registration function
def register(database, username):
    if username in database:
        print(f"Username Exist!")
        return ""
    else:
        print(f"\nRegistration successful")
        return username
