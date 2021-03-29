import socket
import threading
from time import sleep


def ReceiveData():
    # global d, key
    while True:
        try:
            # data, addr = sock.recvfrom(1024)
            # print(data.decode('utf-8'))

            name = sock.recvfrom(1024)
            print(name)
            data = sock.recvfrom(1024)
            print(data)
            # d = data.decode()

            # if d != 'cstop':
            #     crypt = ''
            #     for i in d:
            #         crypt += chr(ord(i) ^ key)
            #     d = crypt

            # print(d)
        except:
            pass


def print_messages():
    print("ds yf 'nfgt print messages")
    # try:
    # if sock.recv(1024)
    name = sock.recv(1024)
    print(name)
    data = sock.recv(1024)
    print(data)
    # except Exception as e:
    #     print(e)


def send_messages():
    while True:
        message = input("Введите сообщение: ")
        sock.send(message.encode())


sock = socket.socket()
print("Начало соединения с сервером!")
address = input("Введите адрес для подключения: ")
if not address or address == '':
    address = "localhost"

port = input("Введите номер порта: ")
if not port or port == '':
    port = 9090
sock.connect(('localhost', 9090))

connection = True

nickname = input("Введите свой никнейм: ")
# msg = nickname
print("Началась отправка никнейма серверу!")
sock.send("user1".encode())  # TODO: back to msg


# while True:
    # sock.close()
    # send = input()
    # msg = send
    # sock.send(msg.encode())

# thread_server = threading.Thread(target=ReceiveData())
thread_server1 = threading.Thread(target=send_messages())
# thread_server.start()
thread_server1.start()
# while True:
#     send = input("Введите сообщение: ")
#     msg = send
#     sock.send(msg.encode())

# thread_server1 = threading.Thread(target=send_messages())
    # print("Прием данных от сервера!")
    # data = sock.recv(1024)
    # print(data)
    # print(data.decode())


