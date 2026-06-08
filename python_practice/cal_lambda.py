def calculator(num1,num2,operd):
    if operd == '+':
        add = lambda num1,num2 : num1 + num2
        return add(num1,num2)
    if operd == '-':
        sub = lambda num1,num2 : num1 - num2
        return sub(num1,num2)
    if operd == '*':
        mul = lambda num1,num2 : num1 * num2
        return mul(num1,num2)
    if operd == '/':
        div = lambda num1, num2 : num1/num2
        return div(num1,num2)
    

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
operd = input("Enter a operd(+,-,*,/):")

result = calculator(num1,num2,operd)
print(result)