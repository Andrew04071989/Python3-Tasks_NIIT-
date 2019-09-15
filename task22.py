# Задание 22:
# Реализовать запуск функции, осуществляющей операцию сложения
# для различных типов (integer,string,list)
# параллельно с различными наборами аргументов.
from multiprocessing import Pool


def var_add(x):
    return x + x


if __name__ == '__main__':
    pool = Pool(processes=5)
    res = pool.map(var_add, 'String')
    res_1 = pool.map(var_add, range(10))
    res_2 = pool.map(var_add, [1, 'abc', [22, 'xyz']])
    res_3 = pool.map(var_add, [1000, 'cab', [range(1000), 'xyz']])
    res_4 = pool.map(var_add, [333, 'ccc', [0, 'xyz']])
    res_5 = pool.map(var_add, ['ddd', 'abc', [None, 'xyz']])
    print(res, '\n', res_1, '\n', res_2, '\n', res_3, '\n', res_4, '\n', res_5)

