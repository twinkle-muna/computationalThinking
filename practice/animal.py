class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
my_dog = Dog(name = "Buddy")
my_cat = Cat(name = "Whiskers")

print(my_dog.speak())
print(my_cat.speak())