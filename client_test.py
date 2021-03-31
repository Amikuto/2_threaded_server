import socket
import threading


def print_messages():
    print("ВЫ на этапе принта мессагей")
    while True:
        try:
            name = sock.recv(1024)
            data = sock.recv(1024)
            print(f"{name.decode()}:    {data.decode()}")
        except Exception as e:
            print(e)
    # else:


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
print("Началась отправка никнейма серверу!")
sock.send("user2".encode())  # TODO: back to msg


thread_server1 = threading.Thread(target=send_messages())
# thread_server1.start()

thread_server = threading.Thread(target=print_messages())
# thread_server.start()

# thread_server.start()
# while True:
#     print(123)


# while True:
#     sock.close()
#     send = input()
#     msg = send
#     sock.send(msg.encode())
#
#     print("Прием данных от сервера!")
#     data = sock.recv(1024)
#     print(data)
#     print(data.decode())