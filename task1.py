# Задание 1:
# Написать и вызвать функцию, принимающую два числа и
# выводящую на экран большее из двух.


# Вариант 1
def max_num(a, b):
    if a == b:
        print('Числа равны')
    else:
        print(max(a, b))


max_num(2, 3)
max_num(22, 33)
max_num(1, 1)


# Вариант 2
def max_num(a, b):
    if a > b:
        print(a)
    elif b == a:
        print('Числа равны')
    else:
        print(b)


max_num(2, 3)
max_num(22, 33)
max_num(1, 1)

