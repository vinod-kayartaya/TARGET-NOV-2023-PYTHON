from threading import Thread


def display_customer_info(file):
    for line in file:
        data = line.split(',')
        customer_name = f'{data[1]} {data[2]}'
        print(customer_name)


def main():
    with open("customers.csv") as f:
        t1 = Thread(target=display_customer_info, args=(f, ))
        t1.start()
        t1.join()

    print('end of main()')


if __name__ == '__main__':
    main()
