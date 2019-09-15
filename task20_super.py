# Задание 20:
# Создайте класс User, в котором будут следующие поля:
# name(имя), age(возраст), методы setName, getName, setAge, getAge.
# Создайте класс Worker, который наследуется от класса User и
# имеет дополнительное поле salary(зарплата),
# а также методы getSalary и setSalary.
# Создайте объект этого класса name='John', age=25, salary=1000.
# Создайте второй объект этого класса 'Jack', age=26, salary=2000.
# Найдите сумму зарплат объектов John и Jack.
# Вариант с super()


class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self.name

    def set_age(self, age):
        self.age = age
        return self.age

    def get_age(self):
        return self.age


class Worker(User):
    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary
        return self.salary

    def get_salary(self):
        return self.salary


a1 = Worker('John', 25, 1000)
a2 = Worker('Jack', 26, 2000)
a_sum = a1.get_salary() + a2.get_salary()
print(a_sum)



