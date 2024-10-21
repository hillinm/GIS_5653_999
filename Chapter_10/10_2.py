import sys
import getopt

opts, args = getopt.getopt(sys.argv, "?hH")

class Dog:
    species = "Canis familiris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
print(miles.description())
print(miles.speak("Woof Woof"))

print(miles)