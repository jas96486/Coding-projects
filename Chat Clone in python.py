import socket # this socket function is used to bulid the network connectivity
import threading # Threading function is used to setup the target between server side and client side.

HOST = '10.0.0.84'# host is ip address of the client machine
PORT = 9090 # port is port address of the client machine

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST, PORT)

server.listen() # listen function is listening the request of the server and client side

clients = []
nicknames = []


def broadcast(message): # here broadcast is casting the network of the client like sending messages
    for client in clients:
        client.send(message)

def handle(client): # handle function is used to handling the client side
    while True:
        try:    # here i used try and except function in which the client didn't recevie any message and it will never show any error because index function will handle it
            message = client.recv(1024)
            print(f'{nicknames[clients.index(client)]} says {message}')
            broadcast(message)
        except:
            index = clients.index(clients)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive(): # receive function is to recevie the request of the client and server side in which it will print that server is runing
    while True:
        client, address = server.accept()
        print(f'Connect with {str(address)}')


        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')

        broadcast(f'{nickname} connected to the server!\n'.encode('utf-8'))
        client.send('connect to the server'.encode('utf-8'))

        thread= threading.Thread(target=handle,args=(client))

print('server runing')
receive()
