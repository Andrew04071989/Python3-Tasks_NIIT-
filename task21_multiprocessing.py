# Задание 21 (c использованием Multiprocessing):
# Написать функцию find_primes(end,start), которая ищет
# все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end.
# Далее необходимо: Запустить ее три раза
# в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# каждый раз в отдельном процессе с помощью multiprocessing.Process.
# Замерить время исполнения каждого варианта и сравнить результаты.
import multiprocessing
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


if __name__ == '__main__':
    pr_1 = multiprocessing.Process(name='Process 1', target=find_primes, args=(10000,))
    pr_2 = multiprocessing.Process(name='Process 2', target=find_primes, args=(20000, 10001))
    pr_3 = multiprocessing.Process(name='Process 3', target=find_primes, args=(30000, 20001))
    timer_start_1 = time.time()
    pr_1.start()
    pr_1.join()
    timer_start_2 = time.time()
    pr_2.start()
    pr_2.join()
    timer_start_3 = time.time()
    pr_3.start()
    pr_3.join()
    timer_end = time.time()
    print('Process 1: //{0:03.2f} sec.//'.format(timer_start_2 - timer_start_1))
    print('Process 2: //{0:03.2f} sec.//'.format(timer_start_3 - timer_start_2))
    print('Process 3: //{0:03.2f} sec.//'.format(timer_end - timer_start_3))
    print('Total wait time : //{0:03.2f} sec.//'.format(timer_end - timer_start_1))