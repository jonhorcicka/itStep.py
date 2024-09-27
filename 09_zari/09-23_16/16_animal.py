class Animal:
    def __init__(self, name):
        self._name = name
    
class Dog(Animal):
    def sound(self):
        print(self._name + ": haf haf")

class Cat(Animal):
    def sound(self):
        print(self._name + ": mňau")

my_dog = Dog('Stark')
my_dog.sound()

my_cat = Cat('Dizzy')
my_cat.sound()

print(my_dog._name)
print(my_cat._name)


