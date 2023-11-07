"""
Basics of OOP in Python
"""


class Person:
    def __init__(self, name=None, city=None):
        print(dir(self))
        self.name = name
        self.city = city
        print(dir(self))
        print(f'Person.__init__ is called with self as {id(self)}')

    def print_info(self):
        print(f'id of self in print_info is {id(self)}')
        print(f'Name = {self.name} and city = {self.city}')


def main():
    p1 = Person('Vinod', 'Bangalore')
    p2 = Person('Shyam', 'Shimoga')
    print(f'id of p1 in main is {id(p1)}')
    p1.print_info()
    p2.print_info()


if __name__ == '__main__':
    main()
