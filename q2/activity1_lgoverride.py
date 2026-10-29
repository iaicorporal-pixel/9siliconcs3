class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "eats food.")

    def make_sound(self):
        print(self.name, "makes a sound.")


class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly!")

    def eat(self):
        print(self.name, "eats fresh meat.")


class Elephant(Animal):
    def make_sound(self):
        print(self.name, "trumpets!")

    def eat(self):
        print(self.name, "eats grass and fruits.")


class Monkey(Animal):
    def make_sound(self):
        print(self.name, "chatters!")

    def eat(self):
        print(self.name, "eats bananas.")


lion1 = Lion("Simba")
elephant1 = Elephant("Dumbo")
monkey1 = Monkey("George")

animals = [lion1, elephant1, monkey1]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print("-----")