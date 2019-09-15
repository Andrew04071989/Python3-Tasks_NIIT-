# Задание 21:
# Написать функцию find_primes(end,start), которая ищет
# все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end.
# Далее необходимо: Запустить ее три раза последовательно
# в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Замерить время исполнения каждого варианта и
# сравнить результаты.
import time


def find_primes(end, start=3):
    li = []
    counter = 0
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                counter += 1

        if counter == 0:
            li.append(i)
        else:
            counter = 0
    return li


timer_start_1 = time.time()
find_primes(10000)
timer_start_2 = time.time()
find_primes(20000, 10001)
timer_start_3 = time.time()
find_primes(30000, 20001)
timer_end = time.time()
print('1: //{0:03.2f} sec.//'.format(timer_start_2 - timer_start_1))
print('2: //{0:03.2f} sec.//'.format(timer_start_3 - timer_start_2))
print('3: //{0:03.2f} sec.//'.format(timer_end - timer_start_3))
print('Total wait time : //{0:03.2f} sec.//'.format(timer_end - timer_start_1))