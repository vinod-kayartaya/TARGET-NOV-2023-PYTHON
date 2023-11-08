"""
Thread features
"""
import time
from threading import Thread


def task1():
    while True:
        print('...printing forever...')
        time.sleep(0.5)


def main():
    t1 = Thread(target=task1, daemon=True)
    t1.start()

    for i in range(10):
        print(f'main() has i as {i}')
        time.sleep(0.25)


if __name__ == '__main__':
    main()
    print('end of script')
