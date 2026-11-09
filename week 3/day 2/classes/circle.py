import math
from classes.shape import Shape

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self) -> float:
        return math.pi * self.radius ** 2