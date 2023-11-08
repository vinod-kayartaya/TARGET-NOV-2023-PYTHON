import json
import socket


def menu():
    print("""
    Here are your options:
    1. Factorial
    2. Fibonacci
    3. Power
    4. Exit
    """)
    return int(input('Enter your choice: '))


if __name__ == '__main__':
    while True:
        choice = menu()
        args = []
        if choice == 1:
            method_name = 'factorial'
            arg = int(input('Enter input for factorial: '))
            args.append(arg)
        elif choice == 2:
            method_name = 'fibonacci'
            arg = int(input('Enter input for fibonacci: '))
            args.append(arg)
        elif choice == 3:
            method_name = 'power'
            arg1 = int(input('Enter value for base: '))
            arg2 = int(input('Enter value for power: '))
            args += [arg1, arg2]
        elif choice == 4:
            break

        message = dict()
        message['method_name'] = method_name
        message['args'] = args

        msg = json.dumps(message)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 1234))
        s.send(msg.encode('utf-8'))
        # need to recv the response from server and display the same

        s.close()