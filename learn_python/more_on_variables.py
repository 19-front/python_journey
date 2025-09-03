# more of variables
num = 5
# check the address of the variable num
id(num)
print(id(num))
name = "navin"
print(id(name))
# now address in detail
a = 10
b = a
print(id(a))
print(id(b))
print(id(10))
# all variables referencing to the same data has the same address
k = 10
print(id(k))
print(id(10))

