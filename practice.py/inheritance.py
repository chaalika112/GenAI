class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d1 = Dog()

d1.eat()

#2
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

c1 = Car()
c1.start()