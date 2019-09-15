# Задание 24 (Сервер):
# Напишите эхо-сервер, работающий по TCP,
# и unit-тест к нему.
# Сервер должен просто возвращать обратно то,
# что передает ему клиент.
import socket


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True
        print('Server is up')
        while self._running:
            conn, address = self._socket.accept()
            print('Server got connection from {}'.format(address))
            m = conn.recv(1024)
            conn.send(m)
            conn.close()


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=1233)
    srv.run()

