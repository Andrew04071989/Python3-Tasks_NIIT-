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
import sqlite3


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    @staticmethod
    def base_create():
        con = sqlite3.connect('sqlite.db')
        print('База данных открыта')
        # Создаем таблицу
        con.execute('CREATE TABLE PLAYLIST'
                    '    (ID         INT      PRIMARY KEY   NOT NULL,'
                    '     SINGER     TEXT                   NOT NULL,'
                    '     TRACK      TEXT                   NOT NULL,'
                    '     ALBUM      TEXT                   NOT NULL,'
                    '     YEAR       INT,'
                    '     DURATION   TIME);')
        print('Таблица создана')
        # Добавляем данные
        con.execute("INSERT INTO PLAYLIST (ID, SINGER, TRACK, ALBUM, YEAR, DURATION)"
                    "VALUES (1, 'Enter Shikari', 'The Last Garrison', "
                    "'The Mindsweep', 2014, '00:03:42')")
        con.execute("INSERT INTO PLAYLIST (ID, SINGER, TRACK, ALBUM, YEAR, DURATION)"
                    "VALUES (2, 'Arctic Monkeys', 'Arabella', "
                    "'AM', 2013, '00:03:27')")
        con.execute("INSERT INTO PLAYLIST (ID, SINGER, TRACK, ALBUM, YEAR, DURATION)"
                    "VALUES (3, 'System of a Down', 'Lonely Day', '"
                    "Hypnotize', 2005, '00:03:09')")
        con.execute("INSERT INTO PLAYLIST (ID, SINGER, TRACK, ALBUM, YEAR, DURATION)"
                    "VALUES (4, 'Foo Fighters', 'The Pretender', "
                    "'Echoes, Silence, Patience & Grace', 2007, '00:04:29')")
        con.execute("INSERT INTO PLAYLIST (ID, SINGER, TRACK, ALBUM, YEAR, DURATION)"
                    "VALUES (5, 'Fall Out Boy', 'Centuries', "
                    "'American Beauty/American Psycho', 2015, '00:03:48')")
        con.commit()
        print('Данные добавлены')
        # Проверяем, что получилось
        cursor = con.execute('SELECT * FROM '
                             'PLAYLIST')
        return cursor

    @staticmethod
    def base_row_choose(row_id):
        con = sqlite3.connect('sqlite.db')
        cursor = con.execute('SELECT * FROM '
                             'PLAYLIST WHERE id={}'.format(int(row_id)))
        for row in cursor:
            return row

    @staticmethod
    def base_del():
        con = sqlite3.connect('sqlite.db')
        con.execute('DROP TABLE PLAYLIST')
        print('Таблица удалена')
        con.close()

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self.host, self.port))
        try:
            self.base_create()
        except sqlite3.OperationalError:
            print('table PLAYLIST already exists')
        self._socket.listen(5)
        self._running = True
        print('Server is up')
        while self._running:
            conn, address = self._socket.accept()
            print('Server got connection from {}'.format(address))
            m = conn.recv(1024)
            message = self.base_row_choose(m)
            conn.send(str(message).encode())
            self.base_del()
            conn.close()


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=1233)
    srv.run()

