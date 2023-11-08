"""
Example of multiple inheritance in Python
"""

class Base1:
    def __init__(self):
        print('Base1.__init__() called')
    def hello(self):
        print('Hello')

class Base2:
    def __init__(self):
        print('Base2.__init__() called')
    def welcome(self):
        print('Welcome')

class Subclass(Base1, Base2):
    def __init__(self):
        super().__init__()
        Base2.__init__(self)
        print('Subclass.__init__() called')


    def hello(self, name):
        print(f'hello {name} from subclass')

    def hello(self):
        print('hello from subclass')

def main():
    s1 = Subclass()
    s1.hello()
    s1.welcome()


if __name__ == '__main__':
    main()
