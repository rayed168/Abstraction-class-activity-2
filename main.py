from abc import ABC
from abc import abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk on two legs")
class Dog(Animal):
    def move(self):
        print("I can walk on four legs")
class Snake(Animal):
    def move(self):
        print("I can slither ")
human1=Human()
human1.move()
dog1=Dog()
dog1.move()
snake1=Snake()
snake1.move()
       