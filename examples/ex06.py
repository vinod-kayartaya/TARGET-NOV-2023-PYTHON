"""
Example for using `for` loop over a collection (like a list or tuple)
"""


def main():
    value = input('Enter employee details separated using a semicolon: ')
    # for example - 101;Vinod Kumar;Male;vinod@vinod.co
    values = value.split(';')

    for index, data in enumerate(values):
        print(f'value at index {index} is `{data}`')


if __name__ == '__main__':
    main()
