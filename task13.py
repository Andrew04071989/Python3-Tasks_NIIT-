# Задание 13:
# Подобрать те функции библиотеки itertools,
# которые дадут правильные ответы на следующие вопросы:


from itertools import chain, filterfalse
from itertools import permutations


# 1) Функция должна принимать три массива ([1,2,3], [4,5], [6,7]),
# а вернуть лишь один массив ([1,2,3,4,5,6,7])
def three_to_one():
    abc = list(chain(a, b, c))
    return abc


#  2) Функция принимает массив (['hello', 'i', 'write', 'cool', 'code'])
# и возвращает массив из элементов,
# у которых длина не меньше пяти (['hello', 'write'])
def less_then_five(i):
    n = len(i)
    return n < 5


#  3) Функция выдает на строку 'password' все возможные комбинации вида
# ([('p','a','s','s'), ('p','a','s','w'), ('p','a','s','o'), ...)
def all_combinations(s):
    li = []
    for item in permutations(s, 4):
        li.append(item)
    return li


# 1)
a = [1, 2, 3]
b = [4, 5]
c = [6, 7]
print("input: ", "\n", a, "\n", b, "\n", c)
print("output: ", "\n", three_to_one(), "\n\n")

# 2)
d = ['Hello', 'I', 'write', 'cool', 'code']
print("input: ", "\n", d)
print("output: ", "\n", list(filterfalse(less_then_five, d)), "\n\n")

# 3)
s = list('password')
print("input: ", "\n", s)
print("output: ", "\n", all_combinations(s))

