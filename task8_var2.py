# Задание 8 (Вариант 2):
# Есть список списков (матрица).
# Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию,
# которая удаляет столбец, содержащий заданную цифру.
matrix = [[10, 2, 3, 5, 7],
          [3, 5, 99, 100, 21],
          [0, 8, 7, 4, 3],
          [1, 9, 3, 1, 2],
          [12, 11, 111, 661, 77]]
print(matrix)
z = int(input('Выберите и введите число из матрицы: '))


def kick_column():
    result = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    edited = [result[j] for j in range(len(result)) if z not in result[j]]
    finish = [[row[i] for row in edited] for i in range(len(edited[0]))]
    return finish


print(kick_column())
