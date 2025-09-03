# dict
data = {1:"navin", 2:"kiran", 4:"harsh"}
print(data)
print(data[4])
print(data[1])
# using get to retrive data to avoid error when key does not exist
data.get(1)
print(data.get(1))
print(data.get(3))
print(data.get(1, "Not found"))
print(data.get(3, "Not found"))
# merging two list together as key and values
keys = ["navin", "kiran", "harsh"]
Values = ["python", "java", "js"]
data = dict(zip(keys, Values)) #use "dict" to convert to dict as 
# key and value after using zip to join the list
print(data)
print(data["kiran"])
# adding new key and value
data ["monica"] = "cs"
print(data)
# delete a key and value
del data["harsh"]
print(data)

# how to create new dict with dicts and lists inside
prog = {"js": "atom", "cs": "vs", "python":["pycham","sublime"],"java":{"jse":"netbeans","jee":"eclipse"}}
print(prog["js"])
print(prog["python"])
print(prog["python"][1])
print(prog["java"])
print(prog["java"]["jee"])