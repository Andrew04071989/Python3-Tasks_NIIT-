# Задание 18:
# Написать функцию to_title: принимает строку,
# ищет пробелы, первые буквы после них и
# после начала строки делает заглавными.
# a = input("Введите текст: ")


def to_title(a):
    b = a.split()
    i = 0
    while i < len(b):
        b[i] = b[i].capitalize()
        i += 1
    n = ' '
    return n.join(b)


t = input('Enter lowercase text: ')
print(to_title(t))
