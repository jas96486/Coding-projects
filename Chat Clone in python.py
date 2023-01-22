import socket # this socket function is used to bulid the network connectivity
import threading # Threading function is used to setup the target between server and client side.

HOST = '10.0.0.84'# host is ip address of the client machine
PORT = 9090 # port is port address of the client machine

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST, PORT)

server.listen() 

clients = []
nicknames = []


def broadcast(message): # here broadcast is casting the network of the client
    for client in clients:
        client.send(message)

def handle(client): 
    while True:
        try:    # try and except function is used for stopping any error message between client side and server side
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


def receive(): # receive function is to used to check client and server status
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
