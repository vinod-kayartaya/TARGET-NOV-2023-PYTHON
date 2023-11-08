"""
A simple client program to the greetings server
"""

import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.149.156', 1234)
    client_socket.connect(addr)

    username = input('What is your name? ')
    client_socket.send(username.encode('ascii'))

    resp = client_socket.recv(1024)
    message = resp.decode('ascii')
    print(f'the server says - {message}')
    client_socket.close()


if __name__ == '__main__':
    main()
