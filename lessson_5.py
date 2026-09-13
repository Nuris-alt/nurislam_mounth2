class Fly:
    def flying(self):
        print('лечу')
class Swim:
    def swim(self):
        print('плыву')
class Duck(Fly, Swim):
    pass
donald = Duck()
donald.swim()
donald.flying()