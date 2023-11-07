"""
Example to read text file
"""


# filename = '/Users/vinod/Desktop/TARGET-NOV-2023-PYTHON/examples/ex01.py'
filename = './ex01.py'


def file_read_example_1():
    f = open(filename, mode='rt')
    content = f.read()
    print(content)
    f.close()


def file_read_example_2():
    with open(filename) as f:
        while True:
            line = f.readline()
            if line == '':
                break
            print(line, end='')


def file_read_example_3():
    with open(filename) as f:
        for line in f:
            print(line, end='')


def main():
    file_read_example_3()


if __name__ == '__main__':
    main()
