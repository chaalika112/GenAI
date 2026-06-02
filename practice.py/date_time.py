# import datatime is a module used to know the 
# date
# time
# curent time
# day/month/year
# time calculations 

import datetime

x = datetime.datetime.now()
print(x)

y = datetime.date.today()
print(y)

z = datetime.time()
print(z)

a = datetime.datetime.now()
print(a.year)
print(a.month)
print(a.day)
print(a.time()) 

name = input("Enter your name:")

today = datetime.date.today()

print("Hello", name)
print("Today's date is: ", today)