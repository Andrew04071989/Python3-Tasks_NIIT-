# Задание 2:
# Написать и вызвать функцию, принимающую два числа и
# возвращающую большее из двух.


# Вариант 1
def max_num(a, b):
    if a == b:
        return 'Числа равны'
    else:
        return max(a, b)


print(max_num(2, 3))
print(max_num(33, 22))
print(max_num(1, 1))


# Вариант 2
def max_num(a, b):
    if a > b:
        return a
    elif a == b:
        return 'числа равны'
    else:
        return b


print(max_num(2, 3))
print(max_num(33, 22))
print(max_num(1, 1))
