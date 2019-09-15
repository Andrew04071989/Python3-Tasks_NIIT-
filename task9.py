# Задание 9:
# Написать класс Man, который принимает имя в конструкторе.
# Имеет метод solve_task, который выводит текст,
# используя имя.


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("This program was launched by {}!".format(self.name))


x = Man('Andrew')
x.solve_task()
