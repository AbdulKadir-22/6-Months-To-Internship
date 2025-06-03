
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} does eat")

    def sleep(self):
        print(f"{self.name} does sleep")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

dog = Dog("Gete")

print(dog.name)
dog.eat()
