#abstraction
from abc import ABCMeta, abstractmethod
class shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(shape):
    def __init__(self):
        self.l=3
        self.b=4
    def printarea(self):
        return self.l*self.b
a=Rectangle()
print(a.printarea())