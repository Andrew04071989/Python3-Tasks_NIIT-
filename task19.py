# Задание 19:
# Написать функцию count_symbol:
# считает сколько раз символ встречается в строке.
a = input("Введите текст: ")
b = input('Введите символ для подсчета: ')


def count_symbol(string, symbol):
    i = 0
    j = 0
    while i < len(a):
        if symbol == string[i]:
            j += 1
        i += 1
    return j


print(count_symbol(a, b))


