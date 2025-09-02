# list
nums = [12,34,87,45,98,22.5,65]
print(nums)
print(nums[4])
print(nums[2:])
print(nums[-1])
print(nums[-5])

names = ["navins", "kiran", "john"]

values = [9.5, "navis", 24]
mil = [nums, names, values]
print(mil)
nums.append(45)
nums.insert(2, 77) #will insert at a index location 
print(mil)
nums.remove(12) #remove a particular element
print(mil)
nums.pop() #this one will remove item at the last
print(mil)

del nums[2:]
print(mil)
nums.extend([12, 12,47])
print(mil)
values.extend(["Vic", 267, 726, 98,321,90.4, "had"])
print(mil)

print(min(nums))
print(max(nums))
print(sum(nums))
bi = nums.sort()
print(bi)
print(mil)