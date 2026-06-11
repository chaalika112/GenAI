#Print 5 fruits in a list
#Add Mango to the end of the list
#Remove Banana from the list
#print all elements using a for loop()
#count the length of the list without len()


fruits = ["Apple", "Banana", "Pineapple", "Grape", "Melon"]

print(fruits)

for fruit in fruits:
    print(fruit)

count = 0 

for fruit in fruits:
    count = count + 1

print(count)

fruits.append("Mango")

print(fruits)

fruits.remove("Banana")

print(fruits)
