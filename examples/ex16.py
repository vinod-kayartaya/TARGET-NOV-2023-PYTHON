"""
Example for encapsulation
"""


class Person(object):
    """
    A class to represent a person details
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city', 'Bangalore')
        self.age = kwargs.get('age')

    def print_info(self):
        print(f'Name  = {self.name}')
        print(f'Age   = {self.age} years')
        print(f'City  = {self.city}')
        print('-'*50)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def city(self):
        return self.__city.capitalize()

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('age must be a number')
        if value is not None and (value < 0 or value > 120):
            raise ValueError('age must be between 0 and 120')

        self.__age = value

    def __str__(self):
        return f'Person(name="{self.name}", city="{self.city}", age={self.age})'


def main():
    p1 = Person(name='Vinod', age=50)
    p2 = Person(name='Kishore', age=20, city='Vasco')
    p1.age = 30  # creates a new attribute and does not affect the private __aage
    p1.print_info()
    p2.city = 'CHENNAI'
    print(f'{p2.name} lives in {p2.city}')
    p2.print_info()
    print(p1)
    print(p2)
    print(dir(p1))


if __name__ == '__main__':
    main()
