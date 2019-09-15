# Задание 21 (c использованием Treading):
# Написать функцию find_primes(end,start), которая ищет
# все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end.
# Далее необходимо: Запустить ее три раза
# в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# каждый раз в отдельном потоке с помощью threading.Thread.
import threading
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


th_1 = threading.Thread(name='thread 1', target=find_primes, args=(10000,))
th_2 = threading.Thread(name='thread 2', target=find_primes, args=(20000, 10001))
th_3 = threading.Thread(name='thread 3', target=find_primes, args=(30000, 20001))
timer_start_1 = time.time()
th_1.start()
th_1.join()
timer_start_2 = time.time()
th_2.start()
th_2.join()
timer_start_3 = time.time()
th_3.start()
th_3.join()
timer_end = time.time()
print('Thread 1: //{0:03.2f} sec.//'.format(timer_start_2 - timer_start_1))
print('Thread 2: //{0:03.2f} sec.//'.format(timer_start_3 - timer_start_2))
print('Thread 3: //{0:03.2f} sec.//'.format(timer_end - timer_start_3))
print('Total wait time : //{0:03.2f} sec.//'.format(timer_end - timer_start_1))
