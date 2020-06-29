class Animal ():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print('Eating')


class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print('Dog Created')

    def bark(self):
        print('woof')

    def eat(self):
        print('dog eating')

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
