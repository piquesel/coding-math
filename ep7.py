# Coding Math Episode 7 
# Implementing a class vector 
import math


class Vector:
    'Represents a vector class in a two-dimensional geometric coordinates'

    def __init__(self, x=1, y=0):
        'Initialize the vector as unit vector i.e. x=1 and y=0'
        self.x = x
        self.y = y

    def set_x(self, x):
        'Set the value of x for our vector'
        self.x = x

    def get_x(self):
        'Return the value of the x coordinate'
        return self.x

    def set_y(self, y):
        'Set the value of y for our vector'
        self.y = y

    def get_y(self):
        'Return the value of the y coordinate'
        return self.y

    def get_length(self):
        'Calculate and return the length of the vector'
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def set_length(self, length):
        'Calculate x and y based on a new given length'
        angle = self.get_angle()
        self.x = math.cos(angle) * length
        self.y = math.sin(angle) * length

    def set_angle(self, angle):
        'Calculate x and y based on a new given angle'
        length = self.get_length()
        self.x = math.cos(angle) * length
        self.y = math.sin(angle) * length

    def get_angle(self):
        'Return the angle of the vector (x, y)'
        return math.atan2(self.y, self.x)

    def get_info(self):
        print(f"Coordinates: ({self.get_x()} {self.get_y()})")
        print(f"Angle: {self.get_angle()}")
        print(f"Length: {self.get_length()}")

    def add(self, v2):
        return Vector(self.x + v2.get_x(), self.y + v2.get_y())

    def substract(self, v2):
        return Vector(self.x - v2.get_x(), self.y - v2.get_y())

    def multiply(self, val):
        return Vector(self.x * val, self.y * val)

    def divide(self, val):
        return Vector(self.x / val, self.y / val)

    def add_to(self, v2):
        self.x += v2.get_x()
        self.y += v2.get_y()

    def substract_from(self, v2):
        self.x -= v2.get_x()
        self.y -= v2.get_y()

    def multiply_by(self, val):
        self.x *= val
        self.x *= val

    def divide_by(self, val):
        self.x /= val
        self.y /= val


if __name__ == '__main__':
    v1 = Vector(10, 5)
    v1.get_info()

    v1.set_angle(math.pi / 6)
    v1.set_length(100)
    v1.get_info()

    v1 = Vector(10, 5)
    v2 = Vector(3, 4)
    v3 = v1.add(v2)
    v3.get_info()

    v2 = v1.multiply(2)
    v2.get_info()

    v1 = Vector(10, 5)
    v2 = Vector(3, 4)
    v1.add_to(v2)
    v1.get_info()
