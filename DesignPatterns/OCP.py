from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


"""

OCP = open for extension, closed for modification. 
    After you test a class, do not modify, only extend it

"""

# basic approach, violates opne closed principle.
class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        for p in products:
            if p.color == color:
                yield p

        """
        Now if there is additional requirement of adding a more filter like size
        or a combination like size and color etc. 
        2^n combinations for n features.  
        
        We can't keep adding to the same class. 
        """


# Specification Pattern.
"""
    Specification can just be an interface 
"""


class Specification:
    # abstract method
    def is_satisfied(self, item):
        pass
    
   # Overloading the & operator for creating a short cut for AndSpecification below.
    def __and__(self, other):
        return AndSpecification(self, other)

"""
    in c# filter class could be made generic instead of inherited
    class Filter<T> where T:ISpecification     
"""


class Filter:
    # abstract method
    def filter(self, items, spec):
        pass


# for filtering by color
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


# for filtering by size
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

#
# if __name__ == '__main__':
apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

bf = BetterFilter()

print('Green Products')
green = ColorSpecification(Color.GREEN)
greenProducts = bf.filter(products, green)

print('Large products')
large = SizeSpecification(Size.LARGE)
largeProducts = bf.filter(products, large)

print('Large Blue Items')
# basic approach
large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue_products = bf.filter(products, large_blue)

# via the overload
large_blue_new = large & ColorSpecification(Color.BLUE)
large_blue_products_new = bf.filter(products, large_blue_new)
