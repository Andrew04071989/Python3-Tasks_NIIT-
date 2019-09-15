# Задание 14:
# Написать функцию для подсчета количества рабочих дней
# между двумя датами (даты передаются в качестве параметров).
import datetime


n_busy = int(input("Enter number from 1 to 7, "
                   "according to busy days in week: "))


def make_date_list():
    # Другой вариант пользовательского ввода:
    # year_from = int(input("Enter year of first date: "))
    # month_from = int(input("Enter month of first date: "))
    # day_from = int(input("Enter day of first date: "))
    # year_to = int(input("Enter year of second date: "))
    # month_to = int(input("Enter month of second date: "))
    # day_to = int(input("Enter day of second date: "))
    # date_from = datetime.date(year_from, month_from, day_from)
    # date_to = datetime.date(year_to, month_to, day_to)
    date_from = input("Enter first date format YYYY-MM-DD: ")
    date_to = input("Enter second date format YYYY-MM-DD: ")
    date_from = date_from.split(sep='-')
    date_to = date_to.split(sep='-')
    date_from = datetime.date(int(date_from[0]), int(date_from[1]), int(date_from[2]))
    date_to = datetime.date(int(date_to[0]), int(date_to[1]), int(date_to[2]))
    delta = date_to - date_from
    date_list = []
    if delta.days <= 0:
        print("ERROR: Second date earlier or equal first date")
        exit()
        make_date_list()
    else:
        for i in range(delta.days + 1):
            date = date_from + datetime.timedelta(i)
            date_list.append(date)
    return date_list


def count_busy_days():
    counter = 0
    for j in make_date_list():
        if datetime.date.isoweekday(j) <= n_busy:
            counter += 1
    print('Between first and second dates {} working days'.
          format(counter))


count_busy_days()
