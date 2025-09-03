# none is when a variable is not assigned to any data
num = ""
# numeric
int
num = 5
float
num = 2.5
complex
num = 4+2j
bool
num = True or False
print(type(num))
# canvert from one type to another
a = int(num)
b = float(num)
c = complex(a,b)
a>b
k = int(True)
k = int(False)
# range
range(10)
# or
list(range(10))
print(range(10))
print(list(range(10)))

# specific set of values in a range, let say 
# start from 2, ends at 10 diff is 2 (thus even numbers from 0-11)
list(range(2, 11,2))
print(list(range(2, 11, 2)))

# dictionary goes with a set {} bracket and must have a key and values
d = {'navin':'samsung', 'rahul':'iphone','kiran':'oneplus'}
# list all keys
d.keys()
# list all values
d.values()
d['kiran']
# use get to fetch values of specific keys
d.get('rahul')
# add
d['ruth'] = 'honor'
