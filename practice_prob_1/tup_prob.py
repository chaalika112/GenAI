#create a tuple of 5 numbers
#print the first and last elements
#count the no.of elements without using len()
#find the maximum value in a tuple
#find the minimum value in a tuple
#count occurrences of a value
#convert a tuple into a list
#convert a list into a tuple
#unpck a tuple
#find the sum of all numbers in a tuple

numbers = (10, 20, 30, 20, 50)

print(numbers)
print("First element: ", numbers[0])
print("Last element: ", numbers[-1])

for i in range(len(numbers)):
    print(i, numbers[i])

#sum of numbers with builtin function
print("Total sum of the Tuple = ", sum(numbers))

#sum without builin function
total = 0

for num in numbers:
    total = total + num
print("Sum = ", total)


count = 0

for num in numbers:
    count = count + 1
print("No.of elements in a tuple:", count)

sorted_tuple = sorted(numbers)
print("Maximum Value: ", sorted_tuple[-1])
print("Minimum Value: ", sorted_tuple[0])

numbers_list = list(numbers)
print("Converted List from Tuple: ", numbers_list)
print(type(numbers))
print(type(numbers_list))

numbers_tuple = tuple(numbers_list)
print("Converted Tuple from List: ", numbers_tuple)
print(type(numbers_tuple))


print("Enter a value to check",numbers, ":")
target = int(input())

count = 0

for num in numbers:
    if num == target:
        count = count + 1

print("Occurences = ", count)

