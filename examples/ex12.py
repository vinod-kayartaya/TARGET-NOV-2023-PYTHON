"""
Example of creating and using generators

Example function generates a fibonacci number

0 1 1 2 3 5 8 13 21 34 ...
"""


def fibo(limit=10):
    n1, n2 = -1, 1
    # data = []
    for i in range(limit):
        n3 = n1 + n2
        yield n3
        # data.append(n3)
        n1, n2 = n2, n3
    # return data


def main():
    for f in fibo():
        print(f, end=', ')
    print()


if __name__ == '__main__':
    main()
