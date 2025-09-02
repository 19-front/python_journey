#display function
def show_homepage():
    print()
    print("         === DonateMe Homepage ===           ")
    print("---------------------------------------------")
    print("| 1.    Login        | 2.    Register       |")
    print("---------------------------------------------")
    print("| 3.    Donate       | 4.    Show Donations |")
    print("---------------------------------------------")
    print("|                 5.   Exit                 |")
    print("---------------------------------------------")

    print()

#donation list
donations = []

#donation function
def donate(username):
    while True:
        donation_input = input(f"\nEnter amount to donate; ")
        if donation_input.isdigit() and int(donation_input) > 0:
        # donation_string = f"{username} donated ${donation_amt}"
            donation_amt = float(donation_input)
            print(f"\nThank you for your generosity, {username} donated ${donation_amt}!")
            return (username, donation_amt)
        else:
            print("\nPlease Enter a positive number.")
            break
            

#showing donation function
def show_donations(donation):
    print("\n--- All Donations ---")
    if len(donation) == 0:
        print("\nCurrently, there are no donations.")
    else:
        total_donation = 0
        for donation in donations:
            print(f"{donation[0]} donated ${donation[1]}")
            total_donation += donation[1]
        print(f"Total = ${total_donation}")