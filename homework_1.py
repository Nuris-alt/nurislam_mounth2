class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"

        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии {self.occupation}, {education}.")


person1 = Person("Али", "01.05.2010", "врач", True)
person2 = Person("Бекжан", "20.08.1980", "электрик", False)
person3 = Person("Расул", "11.11.2002", "учитель", True)


print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

person1.introduce()
person2.introduce()
person3.introduce()