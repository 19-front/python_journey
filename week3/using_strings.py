'''
my_string = "alpha"
'''
'''
multiline_string = """bravo 
charlie
bob"""
print(my_string)
print(multiline_string)

print(my_string[0])
print(my_string[3])

print(my_string[0:3])
print(my_string[:3])
print(my_string[:2])
print(my_string[2:])
print(my_string)

for char in my_string:
    print(char)
    
print("pha" in my_string)
print("z" not in my_string)
print("z" in my_string)
'''
# using f-strings
'''
name = "Alice"
age = 30
greating = f"Hello, my name is {name} and I am {age} years old."
print(greating)
'''

# expression inside f-strings
'''
number = 5
square = f"The square of {number} is {number ** 2}."
print(square)
'''
# combining f-string with string methods
'''
my_string = "hello world"
formatted_string = f"{my_string.upper()} has {len(my_string)} characters."
print(formatted_string)
'''
# formatting numbers with f-strings
'''
pi = 3.14159
formmatted_pi = f"Pi to three decimal places is {pi:.3f}"
print(formmatted_pi)
'''
# combining f-string with multiline strings
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
multiline_fstring = f"""
Name : {name}
Age: {age}
Greeting: {greeting}
"""
print(multiline_fstring)