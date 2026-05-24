def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a>b:
        return a/b
    else:
        return b/a
    

def calculator(num1, num2, operd):
    if operd == '+':
        print(add(num1,num2))
    if operd == '-':
        print(sub(num1,num2))
    if operd == '*':
        print(mul(num1,num2))
    if operd == '/':
        print(div(num1,num2))

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
operd = input("Enter a operd(+,-,*,/):")

calculator(num1,num2,operd)
