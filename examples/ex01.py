"""
Example 01

This is an example module. We are just going to create some basic attributes.
"""

author_name = 'Vinod Kumar'
author_email = 'vinod@vinod.co'
author_website = 'https://vinod.co'


def say_hello():
    """
    just print hello message
    :return: None
    """
    print('Hello, world!')


if __name__ == '__main__':
    print('This is a module called ex01')
    print('The name of this module is ' + __name__)
