"""
Example of class inheritance
"""

from ex16 import Person


class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__eid = kwargs.get('eid')
        self.__salary = kwargs.get('salary', 25000)
        self.__department = kwargs.get('department', 'ADMIN')

    def print_info(self):
        print(f'ID    = {self.__eid}')
        print(f'Salary= {self.__salary} USD')
        super().print_info()

    def __str__(self):
        return (f'Employee(name="{self.name}", eid={self.__eid}, '
                f'department="{self.__department}", salary={self.__salary}, '
                f'age={self.age}, city="{self.city}")')

    def __iadd__(self, value):
        if type(value) is str:
            self.name += value
        elif type(value) in (int, float):
            self.__salary += value
        else:
            raise TypeError('Invalid type of value supplied for +=')
        return self


def main():
    e1 = Employee(name='Scott', salary=34500, eid=2233, city='Dallas')
    print(dir(e1))
    print(e1)
    e1.print_info()

    # e1.__iadd__(' Ross')
    e1 += ' Ross'  # should add ' Ross' to the name
    # e1.__iadd__(1500)
    e1 += 1500     # should increment salary by 1500

    e1.print_info()


if __name__ == '__main__':
    main()

