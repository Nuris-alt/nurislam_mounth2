class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Making sound")

class Dog(Animal):
    def make_sound(self):
        print("гав")
class Cat(Animal):
    def make_sound(self):
        print("мяу")

dog = Dog('Шарик', 2)
cat = Cat('Мурзик', 5)
dog.make_sound()
cat.make_sound()

print(dog.get_name(), dog.get_age())
print(cat.get_name(), cat.get_age())

dog.set_name('Бобик')
dog.set_age(4)

cat.set_age(3)
cat.set_name('Клубок')

print(dog.get_name(), dog.get_age())
print(cat.get_name(), cat.get_age())





