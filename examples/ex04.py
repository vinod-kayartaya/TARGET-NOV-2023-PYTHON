"""
Example for a `while` loop
"""


def main():
    try:
        n = int(input('Enter a number: '))
        i = 1
        while i <= 20:
            print(f'{n} X {i} = {n*i}')
            i += 1

    except ValueError as err:
        print(f'There was an error - {err}')


if __name__ == '__main`__':
    main()
