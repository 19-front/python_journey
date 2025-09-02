
def reverse_string(name):
    stack = []
    for char in name:
        stack.append(char)
    reverse_string = []
    while len(stack) > 0 :
        reverse_string.append(stack.pop())
    return ''.join(reverse_string)

name = input("What is your name? ")
print("Your name reversed is:", reverse_string(name))
