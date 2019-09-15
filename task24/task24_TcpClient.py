# Задание 24 (Клиент):
# Напишите эхо-сервер, работающий по TCP,
# и unit-тест к нему.
# Сервер должен просто возвращать обратно то,
# что передает ему клиент.
import socket
import random


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        message = input('enter text: ')
        self.socket.send(message.encode())
        print('message send: {}'.format(message))
        data = self.socket.recv(1024)
        print('Received: {}'.format(data.decode()))
        self.socket.close()


if __name__ == '__main__':
    name = 'Python client ' + str(random.randint(1, 1000))
    my_client = TcpClient(host='127.0.0.1', port=1233)
    my_client.run()
