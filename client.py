import socket


def ReceiveData():
    while True:
        try:

            name = sock.recvfrom(1024)
            print(name)
            data = sock.recvfrom(1024)
            print(data)
        except:
            pass


def print_messages():
    print("ds yf 'nfgt print messages")
    name = sock.recv(1024)
    print(name)
    data = sock.recv(1024)
    print(data)


def send_messages():
    while True:
        message = input("Введите сообщение: ")
        sock.send(message.encode())


if __name__ == "__main__":
    sock = socket.socket()

    print("Начало соединения с сервером!")
    address = input("Введите адрес для подключения: ")
    if not address or address == '':
        address = "localhost"

    port = input("Введите номер порта: ")
    if not port or port == '':
        port = 9090
    sock.connect(('localhost', 9090))

    # connection = True

    while True:
        nickname = input("Введите свой никнейм: ")
        if len(nickname) != 0:
            print("Началась отправка никнейма серверу!")
            sock.send(nickname.encode())
            break
        else:
            continue
            # nickname = input("Введите свой никнейм: ")
    while True:
        send = input()
        msg = send
        sock.send(send.encode())
        data = sock.recv(1024)
        print(data.decode())
