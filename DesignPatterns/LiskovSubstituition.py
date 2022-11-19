class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self,size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


""" 
    This function is supposed to work on all rectangles. 
    But as we pass square- a derived class of rectange, the method does not work. 
    This is a violation of Liskov Substitution Principle.
    
    This method is supposed to accept a rectangle. Set its height to 10 and print the area. 
    But as soon as we pass square, both height and width get updated due to above setters. 
    This leads to wrong output. 
    
    Possible fixes - No need of Square. 
    1. Have a property in rectange that can tell if it is a square
    2. Or implement a factory method to create squares. 
"""
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected Aread : {expected}, Got: {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)