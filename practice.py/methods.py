# List Methods
# extend method

a = [1, 2]
a.extend([3, 4])

print(a)

# insert method

names = ["chaalika", "chukka"]
names.insert(1, "b")

print(names)

# remove method

fruits = ["apple", "banana"]
fruits.remove("banana")

print(fruits)

# pop() method

numbers = [10, 20, 30]
numbers.pop(1)

print(numbers)

# sort() method

nums = [5,3,7,8]
nums.sort()

print(nums)

# reverse() method

nums = [1, 2, 3]
nums.reverse()

print(nums)

# index() method

fruits = ["apple", "mango", "banana"]
print(fruits.index("banana"))

# clear() method

a = [1,2,3]
a.clear()

print(a)


# Dictionary Methods
# keys() method

student = {
    "name": "Ram",
    "age": 22
}

print(student.keys())

# values() method

print(student.values())

# items() method

print(student.items())

# get() method

print(student.get("name"))

# update() method

student.update({"address": "Austin"})
print(student)

# pop() method

student.pop("age")
print(student)

# popitme() method

student.popitem()
print(student)

# clear() method

student.clear()
print(student)

# copy() method

new_student = student.copy()
print(new_student)

