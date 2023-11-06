"""
Example of using atrributes of another module
"""

from ex01 import say_hello


if __name__ == '__main__':
    print('This is a module called ex02')
    print('The name of this module is ' + __name__)

    # calling the imported function
    say_hello()



