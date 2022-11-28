from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

""" 
    Without the factory pattern
    
    variables are ambiguous. Not clear what a and b map to. 
    
    if we have to add another coordinate system, it becomes very complex. 
"""
class Point:
    def __init__(self, a, b, system = CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)




class NewPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}   y:{self.y}'

    # factory methods to create different types of points
    @staticmethod
    def new_cartesian_point(x,y):
        return NewPoint(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return NewPoint(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = NewPoint(2, 3)
    p1 = NewPoint.new_cartesian_point(2,3) # p and p1 do the same thing.
    p2 = NewPoint.new_polar_point(1, 2)
    print(p, p2)

