# class car:
#     # метод конструктор, инициализатор
#     def __init__(self,model, color):
#         self.model = model
#         self.color = color
#
#     def drive_to(self, destination):
#         print(f'Машина цвета: {self.color} поехала в {destination}')
#
#
# #создание объекта путём 'вызова' класса
# car1 = car('Kia', 'red')#создание объекта вызывает __init__
# car2 = car('BMW', 'blue')
# print(car1)
# print(car2)
# print(car1.model, car1.color)#обращение к атрибутам объекта
# print(car2.model, car2)
# print(type(car2))#тип объекта
# car1.drive_to("Кант")
# car1.fined = True
# print(car1.fined)



















class GameCharacter:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
character1 = GameCharacter("Nurbek", 25, "Python")
print(character1.name)
print(character1.age)
print(character1.hobby)