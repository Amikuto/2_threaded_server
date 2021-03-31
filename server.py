import errno
import socket
import threading


def accept_client():
    while True:
        cli_sock, cli_add = sock.accept()
        uname = cli_sock.recv(1024)
        CONNECTION_LIST.append((uname, cli_sock))
        print(f"{uname} is now connected")
        thread_client = threading.Thread(target=broadcast_usr, args=[uname, cli_sock])
        thread_client.start()


def broadcast_usr(uname, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                print(f"{uname} пишет: {data}")
                b_usr(cli_sock, uname, data)
        except Exception as ex:
            print(ex)
            break


def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if client[0] == sen_name:
            # client[1].send(sen_name)
            client[1].send(msg)


if __name__ == "__main__":
    sock = socket.socket()

    port = 9090
    while True:
        try:
            sock.bind(('', port))
            print("Сервер запущен на порту -", port)
            break
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Порт уже занят!")
                port += 1
            else:
                print("Ошибка в подключении! ", e)

    sock.listen(1)
    print("Начало прослушивания порта!")

    CONNECTION_LIST = []

    thread = threading.Thread(target=accept_client())
    thread.start()
