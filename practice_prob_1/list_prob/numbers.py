#print largest number without using max()
#print smallest number without using min()
#count how many times a num appears in a list
#print a new list with squares of nubers
#print a reversed list without using reverse() - used slicing

numbers = [10, 25, 8, 42, 15, 10, 15, 72, 10, 2]

numbers.sort()

print("Largest number:", numbers[-1])
print("Smallest number:", numbers[0])
print(numbers)
print(numbers[::-1])

target = int(input("Enter a number from the list: "))

count = 0

for num in numbers:
    if num == target:
        count = count + 1

print("Appears", count, "Times")

squares = []

for num in numbers:
    squares.append(num * num)

print("Squares of the numbers are:", squares)