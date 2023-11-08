"""
concurrency in Python using `threadig` module
"""

import threading


def task1(loop_limit, message):
    for i in range(loop_limit):
        print(f'{message} {i}')


def main():
    t1 = threading.Thread(target=task1, name='thread-001', args=(10, '===> in thread-001, value of i is '))
    t2 = threading.Thread(target=task1, name='thread-002', args=(20, ':::> in thread-002, value of i is '))

    t1.start()
    t2.start()
    for i in range(15):
        print(f'===> value of i in main() is {i}')


if __name__ == '__main__':
    main()
