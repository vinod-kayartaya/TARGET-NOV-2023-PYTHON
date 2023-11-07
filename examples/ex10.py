"""
Example of creating functions with var-args
"""


def add_inputs(*args):
    print(f'type of args is {type(args)}')
    print(f'args is {args}')
    args = [n for n in args if type(n) in (int, float)]
    return sum(args)


def main():
    total = add_inputs(10, 20, 30, 'vinod', 'bangalore', 40)
    print(total)

    data = (1, 2, 3, 2, 1)
    total = add_inputs(*data)
    print(total)


if __name__ == '__main__':
    main()
