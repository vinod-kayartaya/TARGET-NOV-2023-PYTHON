"""
Example of writing and using functions with positional and named parameters
"""


def add_inputs(num1, num2=100):
    if type(num1) not in (int, float) or type(num2) not in (int, float):
        raise TypeError('Invalid type for input. Expected int or float')

    return num1+num2


def main():
    total = add_inputs(10)
    print(total)

    total = add_inputs(10, 20)
    print(total)

    total = add_inputs(num2=100, num1=200)
    print(total)

    t = (12, 34)
    total = add_inputs(*t)
    print(total)


if __name__ == '__main__':
    main()

