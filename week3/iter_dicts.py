state_capitals = {"Washingtom": "Olympia", "Oregon": "Salam", "Califonia": "Sacremento"}

# for state in state_capitals:
#     print(state)
    
# for city in state_capitals.values():
#     print(city)

# for state in state_capitals:
#     print(state_capitals[state], "is a capiatal of", state)
    
for state, city in state_capitals.items():
    print(city, "is a capiatal of", state)
    