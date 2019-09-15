# Задание 15:
# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст и.т.д.).
# Написать функцию, которая создавала бы указанное
# количество экземпляров, сериализовывала их и
# сохраняла в файл human.data,
# и другую функцию, которая бы читала файл human.data,
# десериализовывала его содержимое и
# выводила результат на печать.
# Примечание: чтоб у экземпляров Human
# были разные значения атрибутов,
# можно воспользоваться функциями
# random.randint() и random.choice()
import random
import pickle


class Human:
    def __init__(self):
        self.name = ['Ivan', 'Petr',
                     'Aleksandr', 'Victor',
                     'Igor', 'Vladimir']
        self.surname = ['Ivanov', 'Volkov',
                        'Medvedev', 'Petrov',
                        'Sidorov', 'Putin']
        self.age = range(18, 35)
        self.country = ['Russia', 'USA', 'Canada',
                        'China', 'India', 'Australia']
        self.city = ['Moscow', 'Los Angeles', 'Toronto',
                     'Pekin', 'Deli', 'Sidney']

    def make_person(self):
        n_row = input('Enter number of row: ')
        i = 0
        base = []
        while i < int(n_row):
            name = random.choice(self.name)
            surname = random.choice(self.surname)
            age = random.choice(self.age)
            country = random.choice(self.country)
            city = self.city[self.country.index(country)]
            row = [name, surname, age, country, city]
            base.append(row)
            i += 1
        with open('human.data', 'wb') as p:
            pickle.dump(base, p)

    @staticmethod
    def watch_db():
        with open('human.data', 'rb') as p:
            base = pickle.load(p)
        print(base)


h = Human()
h.make_person()
h.watch_db()


