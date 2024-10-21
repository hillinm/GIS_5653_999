import sys
import getopt

opts, args = getopt.getopt(sys.argv, "?hH")

class Dog:
    species = "Canis familiris"
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
buddy = Dog("Buddy", 9, "white")
miles = Dog("Miles", 4, "black")
philo = Dog("Philo", 5, "brown")
print(miles.description())
print(miles.speak("Woof Woof"))
print(miles)
print(f"{philo.name}'s coat is {philo.coat_color}")
