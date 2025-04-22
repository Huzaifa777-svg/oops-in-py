# Simple Inheritance
# 1-Create a class Animal with a method speak() that prints "Animal sound".
# Then create a class Dog that inherits from Animal.
# Task: Create a Dog object and call speak().

class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    pass
dog=Dog()
dog.speak()


# Method Overriding
# 2- Modify the Dog class to override the speak() method to print "Bark".
# Task: Show that Dog().speak() prints "Bark" instead of "Animal sound".

# Modified Dog class with overridden speak() method
class Dog(Animal):
    def speak(self):
        print("Bark")


dog = Dog()
dog.speak()  
