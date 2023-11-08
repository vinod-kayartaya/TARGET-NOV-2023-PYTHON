"""
Example of a polymorphic method
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def shape_name(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius=1.0):
        self.__radius = radius

    def shape_name(self):
        return 'circle'

    def area(self):
        return 3.14156 * (self.__radius ** 2)


class Rectangle(Shape):
    def shape_name(self):
        return 'rectangle'

    def area(self):
        return self.__side1 * self.__side2

    def __init__(self, side1=1.0, side2=1.0):
        self.__side1 = side1
        self.__side2 = side2


def process_shape(shape: Shape) -> None:
    if not isinstance(shape, Shape):
        print(f'Expected a Shape, but got a value of {type(shape)}')
        return

    print(f'Shape name is {shape.shape_name()}')
    print(f'Area of this {shape.shape_name()} is {shape.area()}')


def main():
    # sh1 = Shape()  # Can't instantiate abstract class Shape with abstract methods area, shape_name
    c1 = Circle(12.34)  # is an instance of Circle and Shape (and object)
    r1 = Rectangle(12, 34)  # is an instance of Rectangle and Shape (and object)
    n1 = 100
    s1 = 'Vinod'

    process_shape(c1)
    process_shape(r1)
    process_shape(n1)
    process_shape(s1)


if __name__ == '__main__':
    main()
