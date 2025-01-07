"""
Object Oriented Programming (OOP)  is a way of organizing code around objects
(e.g. Animals), which represent real-world entities.
Each object encapsulates data (attributes) and behaviour (methods).

Encapsulation:
    Combine data into a single class, this hides unneccessary details that
    simplifies interaction.  Encapsulation in Python refers to the practice of
    bundling data (attributes) and methods (functions) that operate on that
    data into a single unit called a class. This process helps in hiding the
    internal details of how a class works and provides a clear, well-defined
    interface for interacting with it.

Abstraction:
    Focus on the essential features (eg animal here) like it's name and sound
    without worrying about how these features are implimented

Inheritance:
    Create specific animal types (eg Cats and Dogs) from a general Animal
    class.
    Reuse shared behaviour and specialize where needed.

Polymorphism:
    Use the same interface (make_sound) for different animal types.

Composition:
    Use other classes (like Legs or Wings) to describe an animal's features
"""


class Legs:
    def __init__(self, count):
        self.count = count


class Animal:
    def __init__(self, name, leg_count):
        self.name = name      # Private attribute
        self.legs = Legs(leg_count)

    def make_sound(self):
        return "Some generic sound"

    def description(self):
        return f"{self.name} has {self.legs.count} legs."


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Bird(Animal):
    def make_sound(self):
        return "Tweet tweet"


def animal_sound(animal):
    print(animal.make_sound())


dog = Dog("Dog", 4)
cat = Cat("Cat", 4)
bird = Bird("Bird", 2)
spider = Animal("Spider", 8)

print(dog.make_sound())
print(dog.description())
print("====================")
print(cat.make_sound())
print(cat.description())
print("====================")
print(bird.make_sound())
print(bird.description())
print("====================")
print(spider.make_sound())
print(spider.description())
print("====================")

friends = [Dog("Fred", 4), Cat("Wendy", 4), Bird("Boris", 2)]
for friend in friends:
    animal_sound(friend)
