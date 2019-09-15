# Задание 24 (unit-test):
# Напишите эхо-сервер, работающий по TCP,
# и unit-тест к нему.
# Сервер должен просто возвращать обратно то,
# что передает ему клиент.
import unittest
import socket


class TestTcpClient(unittest.TestCase):
    def test_client(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', 1233))
        message = 'Echo'
        print(message)
        self.socket.send(message.encode())
        data = self.socket.recv(1024)
        self.assertEqual(message, data.decode())


if __name__ == '__main__':
    unittest.main()
