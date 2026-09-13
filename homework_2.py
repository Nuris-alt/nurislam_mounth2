class Person:
    def __init__(self, name, age, color, food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food

    def introduce(self):
        print(f'Меня зовут: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Любимый цвет: {self.color}')
        print(f'Любимая еда: {self.food}')

class Classmate(Person):
    def __init__(self, name, age, color, food, group_name):
        super().__init__(name, age, color, food)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print(f'Моя группа: {self.group_name}')

class Friend(Person):
    def __init__(self, name, age, color, food, hobby):
        super().__init__(name, age, color, food)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print(f'Моё хобби: {self.hobby}')


classmate1 = Classmate('Амир', '12', 'синий', 'плов', 'B11')
classmate2 = Classmate('Расул', '22', 'фиолетовый', 'самсы', 'B12')


friend1 = Friend('Айдана', '31', 'красный', 'суп', 'Рисование')
friend2 = Friend('Марат', '24', 'жёлтый', 'блины', 'Баскетбол')

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()