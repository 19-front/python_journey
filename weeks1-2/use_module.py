import my_module
my_module.greet('Albert Agyemang')
print('My favorite ice cream flovor is', my_module.flavor)

# another way of importing, this case only section of the code needed
from my_module import greet, flavor
greet('Albert Agyemang')
print('My favorite ice cream flovor is', flavor)