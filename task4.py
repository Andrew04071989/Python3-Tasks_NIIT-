# Задание 4:
# Составить программу,
# которая будет считывать введённое пятизначное число.
# После чего, каждую цифру этого числа,
# необходимо вывести в новой строке (не используя «enumerate»)


def recursion():
    a = input("Enter five-digit number - ")
    if len(a) == 5 and a.isdigit():
        n = 0
        for i in a:
            n += 1
            print('{} цифра равна {}'.format(n, i))
    else:
        print('Not a five-digit number!')
        recursion()


recursion()


