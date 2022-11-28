class NewPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}   y:{self.y}'

class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return NewPoint(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return NewPoint(rho * cos(theta), rho * sin(theta))



if __name__ == '__main__':
    p = PointFactory.new_cartesian_point(2, 3)
    p2 = PointFactory.new_polar_point(1, 2)
    print(p, p2)
