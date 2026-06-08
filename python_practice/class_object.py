class Student:

    def __init__(self,name,age,college):
        self.name = name
        self.age = age
        self.college = college

    
name = input("Enter your name:")
age = int(input("Enter your age:"))
college = input("Enter your college:")

s1 = Student(name,age,college)

print(s1.name, "-", s1.age, "-", s1.college)

