class Bank:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print("Balance: ", self.__balance)

b1 = Bank()
b1.show_balance()


#2

class Phone:

    def __init__(self):
        self.__battery = 100

    def use_phone(self):
        self.__battery -= 10

    def show_battery(self):
        print(self.__battery)

p1 = Phone()

p1.use_phone()
p1.show_battery()