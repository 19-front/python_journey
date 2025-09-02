state_capitals = {"Washingtom": "Olympia", "Oregon": "Salam", "Califonia": "Sacremento"}
# print(len(state_capitals))
# print(state_capitals["Washingtom"])
# state_capitals["Washingtom"] = "Aberdeen"
# state_capitals["Texas"] = "Austen"
# print(state_capitals)
# del state_capitals["Califonia"]
# print(state_capitals)
# removed_capital = state_capitals.pop("Oregon")
# print(state_capitals)
# print(removed_capital)
for state, city in state_capitals.items():
    state = input("Enter state: ")
    city = input("City: ")
    if state or city in state_capitals:
        print("Yes")
    else: print("no")