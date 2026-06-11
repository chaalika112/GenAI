#creste a dict with student - name, age & grade
#print all keys
#print all values
#Add new key with value
#update students age
#remove a key from the dict
#count the no. of key-value pairs without using len()
#find the highest score
#find the average score
#print only students scoring above 90


students = {
    "student1": {"name": "John", "age": 20, "grade": "74"},
    "student2": {"name": "Mary", "age": 21, "grade": "82"},
    "student3": {"name": "David", "age": 19, "grade": "93"},
    "student4": {"name": "Sarah", "age": 22, "grade": "88"},
    "student5": {"name": "Mike", "age": 20, "grade": "97"}
}

for student in students: 
    print(student, students[student])

for key in students:
    print(key)

for value in students.values():
    print(value)

count = 0

for key in students:
    count = count + 1

print("Number of key - value pairs: ", count)

for student in students.values():
    student["City"] = "Austin"

for student in students:  
    print(students[student])

scores = []

total = 0

for student in students.values():
    score = int(student["grade"])

    scores.append(score)
    total = total + score 

    average = total/count 

    if score >= 90:
        print("Students scoring above 90: ", student["name"])

scores.sort()
print("Highest Score:", scores[-1])
print("Average =", average)


choice = input("Do you want to change a student's age? (yes/no): ")

if choice == "yes": 
   name = input("Enter students name: ")
   new_age = int(input("Enter the updated age: "))

   for student in students.values():
       if student["name"] == name:
          student["age"] = new_age

   print("Age Updated")
   for student in students:
       print(students[student])

else: 
    print("Okay")

choice2 = input("Do you want to remove a key from dict for all 5 students? (yes/no): ")
if choice2 == "yes":
       key = input("Enter key to remove: ")

       for student in students.values():
           del student[key]
       
       for student in students:
           print(students[student])

else:
       print("Okay")
