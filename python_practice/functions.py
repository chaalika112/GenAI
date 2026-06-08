# print("hello pavan")



# def print_name(name):
#     return(f"Hello {name}")

# a = print_name("pavan")
# print (a)


# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mul(a,b):
#     return(a*b)
# def div(a,b):
#     if a > b:
#      return(a/b)
#     else:
#         return(b/a)

# def calculator(num1, num2, operd):
#     if operd == '+':
#         print(add(num1,num2))
#     elif operd == '-':
#         print(sub(num1,num2))
#     elif operd == '*':
#         print(mul(num1,num2))
#     elif operd == '/':
#         print(div(num1,num2))
    
# num1 = int(input("Enter a number:"))
# num2 = int(input("enter a number:"))
# operd = input("enter operd(+,-,*,/):")

# result = calculator(num1,num2,operd)
# print(result)


def calculator(num1, num2, operd):
    if operd == '+':
       add = lambda num1, num2 : num1 + num2
       return add(num1,num2)
    elif operd == '-':
       sub = lambda num1, num2 : num1 - num2
       return sub(num1,num2)
    elif operd == '*':
       mul = lambda num1, num2 : num1 * num2
       return mul(num1,num2)
    elif operd == '/':
       div = lambda num1, num2 : num1 * num2
       return div(num1,num2)
num1 = int(input("Enter a number:"))
num2 = int(input("enter a number:"))
operd = input("enter operd(+,-,*,/):")

result = calculator(num1,num2,operd)
print(result)
