# Задание 23 (Клиент):
# Напишите серверный скрипт, работающий с базой данных sqlite.
# Скрипт должен создавать  таблицу перед тем,
# как начать прослушивание сокета,
# затем принимать запросы от клиентов и
# возвращать записи из этой таблицы по ID в этих запросах.
# Напишите клиентский скрипт,
# который будет подключаться к серверу,
# отправлять id и выводить строку, которую вернет сервер.
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
        message = input('enter ID: ')
        self.socket.send(message.encode())
        print('message send: {}'.format(message))
        data = self.socket.recv(1024)
        print('Received: {}'.format(data.decode()))
        self.socket.close()


if __name__ == '__main__':
    name = 'Python client ' + str(random.randint(1, 1000))
    myclient = TcpClient(host='127.0.0.1', port=1232)
    myclient.run()