class Animal:
    def make_sound(self):
        print("some sound...")

class Dog(Animal):
    def make_sound(self):
        print("woof!")
class Cat(Animal):
    def make_sound(self):
        print("meow!")
class Cow(Animal):
    def make_sound(self):
        print("moo!")

animals = [Dog(),Cat(),Cow()]        
for animal in animals:
    animal.make_sound()