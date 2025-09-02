from donations_pkg import homepage
from donations_pkg import user

#global variables
# database = {"admin": "password123", "bob": "123"}
database = {}

authorized_user = ""

#busines logic
while True:
#display of homepage
    homepage.show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.\n")
    if database != {}:
        print(f"\nLogged in as: {authorized_user}")
    else:
        print("Note: Database is empty, register first")
        
        
        
    user_choice = str(input("\nSelect an option: "))

#login
    if user_choice == "1":
        username = str(input("\nEnter your Username: "))
        username = username.lower()
        password = str(input("\nEnter your Password: "))
        if  authorized_user == user.login(database,username,password):
            print(f"\nLogged in as {authorized_user}")
        if user.login(database,username,password) == "":
            print(f"\nYour {username} and password not registered!\n")
            break
        else: break
#registration
    elif user_choice == "2":                
        username = str(input("\nEnter your new Username: "))
        username = username.lower()
        if not (username[0].isalpha() and username.isalnum()):
            print("\nUsername must start with a letter and contain only alphanumeric characters.\n")
            break
        if len(username) > 10:
            print("\nError: Username must not exceed 10 characters. \nPlease try again.")
            
        password = str(input("\nEnter your new Password: "))
        if len(password) >= 5:
            authorized_user = user.register(database, username)
        if authorized_user !="":
            database[username]=password
            print(f"\nRegistered {authorized_user}")
        else:
            print("\nError: Password must be 5 characters. Please try again.")

#adding donations           
    elif user_choice == "3":
        if authorized_user == "":
            print(f"\nYou are not loggined in")
        else:
            donation_string = homepage.donate(authorized_user)
            homepage.donations.append(donation_string)

#showing donations
    elif user_choice == "4":
        homepage.show_donations(homepage.donations)

#logging out
    elif user_choice == "5":
        print(f"\nGoodbye {username} see you soon!")
        print()
        break