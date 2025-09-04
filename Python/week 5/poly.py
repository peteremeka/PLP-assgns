    # Polymorphism
class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
        

class Cat(Animal):
    def speak(self):
        return "Meow!"
        

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())




   