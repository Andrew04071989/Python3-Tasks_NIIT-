# Задание 10:
# Написать класс Pupil, у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд.
import time
import random


class Pupil:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("This program was launched by {}!".format(self.name))


y = Pupil('Andrew')
y.solve_task()



