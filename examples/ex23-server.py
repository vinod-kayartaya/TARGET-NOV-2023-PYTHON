"""
A simple greetings server
"""

import socket
from threading import Thread


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.149.156', 1234)
    server_socket.bind(addr)
    server_socket.listen(10)
    print('server started')
    while True:
        print('waiting for clients to connect...')
        client_socket, client_addr = server_socket.accept()  # wait for incoming client connections
        print(f'got a connection from a client at address {client_addr}')
        Thread(target=handle_client, args=(client_socket,)).start()


def handle_client(client_socket):
    username = client_socket.recv(1024)
    username = username.decode('ascii')

    print(f'the username is "{username}"')

    message = f'Hello {username}, and welcome to socket programming in Python'
    client_socket.send(message.encode('ascii'))
    client_socket.close()


if __name__ == '__main__':
    main()
