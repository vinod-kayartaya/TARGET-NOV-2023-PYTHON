"""
Example for using the `for` loop and the `range` object
"""


def main():
    try:
        num = int(input('Enter a number: '))
        for i in range(num):
            print('#' * (i+1))
            # for j in range(i+1):
            #     print('#', end='')
            # print()
    except ValueError:
        print('Try only with a number!!')


if __name__ == '__main__':
    main()
