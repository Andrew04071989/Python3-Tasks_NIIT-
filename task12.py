# Задание 12:
# Напишите свой менеджер контекста,
# замеряющий и показывающий время исполнения кода внутри него.
import time


class TestManager:
    def __init__(self):
        pass

    def __enter__(self):
        print('Start')
        self.__enter__ = time.time()
        print(self.__enter__)
        return self.__enter__

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__exit__ = time.time()
        print(self.__exit__)
        print('Время выполнения операции: {} сек.'.
              format(round(self.__exit__ - self.__enter__, 1)))
        print('End')


with TestManager():
    for i in range(1000):
        time.sleep(0.00000001*i)


