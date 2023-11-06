"""
Example to accept a value and use `if` statements
"""


def main():
    m = input('Enter a value for month: ')

    if m.isdigit():
        m = int(m)
    else:
        print(f'`{m}` is not a valid number at all')
        return

    if m < 1 or m > 12:
        print(f'{m} is an invalid number for a calendar month')
    else:
        print(f'{m} is a valid month number')

        if m in (4, 6, 9, 11):
            days = 30
        else:
            days = 28 if m == 2 else 31

        print(f'this month has {days} days in it.')


if __name__ == '__main__':
    main()