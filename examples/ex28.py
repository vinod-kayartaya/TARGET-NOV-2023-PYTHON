from sqlite3 import connect, DatabaseError


def create_customers_table():
    connection_str = 'customers_db.sqlite'
    with connect(connection_str) as conn:
        print('connection to the db created')
        sql_cmd = """create table customers(
        id integer primary key autoincrement,
        name varchar(50) not null,
        email varchar(250) unique,
        phone varchar(50) unique
        )"""
        try:
            cur = conn.cursor()
            cur.execute(sql_cmd)
            print('table customers created')
        except DatabaseError as err:
            print(f'there was an error: {err}')


def add_customer_records():
    connection_str = 'customers_db.sqlite'
    with connect(connection_str) as conn:
        while True:
            name = input('Enter a name: ')
            email = input('Enter email address: ')
            phone = input('Enter phone number: ')
            sql_cmd = 'insert into customers (name, email, phone) values (?, ?, ?)'
            cur = conn.cursor()
            cur.execute(sql_cmd, (name, email, phone))
            ans = input('Do you want to add another (yes/no): [yes] ')
            if ans == 'no':
                break


def search_by_id():
    connection_str = 'customers_db.sqlite'
    with connect(connection_str) as conn:
        cur = conn.cursor()
        cid = int(input('Enter customer id to search: '))
        cur.execute('select * from customers where id = ?', (cid, ))
        rec = cur.fetchone()
        if rec is None:
            print(f'No customer found for id {cid}')
        else:
            print(rec)


if __name__ == '__main__':
    while True:
        print("""
        Main menu:
        1. Create table
        2. Add customer records
        3. Search by id
        4. Exit
        """)
        choice = int(input('What is your choice? '))
        if choice == 1:
            create_customers_table()
        elif choice == 2:
            add_customer_records()
        elif choice == 3:
            search_by_id()
        elif choice == 4:
            break
        else:
            print('Invalid choice!!')

