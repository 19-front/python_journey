states = ["Washington", "Oregon", "Califonia"]

'''
for x in states:
    print(x)
'''

# or use familliar variable name to remember
'''
for state in states:
    print(state)

for state in states:
    state = state.lower()
    print(state)

print()

print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

'''
# concatenating list
states2 = ["Arizona", "Ohio", "Louisiana"]
best_states = states + states2
print(best_states)
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])