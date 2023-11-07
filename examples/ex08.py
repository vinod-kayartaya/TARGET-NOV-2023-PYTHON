"""
Accept a series of values from command-line arguments and print the sum of the same.
The `sum` works only with a list of numerical values.
"""
import sys


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return 0


def main():
    print('hello, world')
    args = [to_float(n) for n in sys.argv]
    print(sum(args))


if __name__ == '__main__':
    main()
