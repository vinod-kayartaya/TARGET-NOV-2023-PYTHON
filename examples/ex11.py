"""
Example of a function that takes keyword arguments

"""


def print_report(**kwargs):
    print(f'type of kwargs is {type(kwargs)}')
    print(f'kwargs is {kwargs}')
    if 'name' not in kwargs or 'salary' not in kwargs:
        raise KeyError('name and salary is mandatory')

    print(f'ID         : {kwargs.get("eid")}')
    print(f'Name       : {kwargs["name"]}')
    print(f'Salary     : {kwargs["salary"]}')
    print(f'Department : {kwargs.get("dept", "ACCOUNTING")}')
    print('-'*50)


def main():
    print_report(name='Rohit', salary=220000, dept='ADMIN', eid=2234)
    data = {'name': 'Miller', 'salary': 90000, 'dept': 'MARKETING'}
    print_report(**data)
    fn1 = print_report
    fn1(name='Robert', salary=120000)


if __name__ == '__main__':
    main()
