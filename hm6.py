'''
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

# first_el = int(input('Введите первый элемент: '))  # a1
# difference = int(input('Введите разность: '))          # d
# count_numbers = int(input('Введите количество элементов: '))  # col
#
# def arithmetic_progression(a1, d, col):
#     array = [a1]
#     for i in range(col):
#         if i != 0:
#             a = a1 + i * d
#             array.append(a)
#     return array
#
# print(arithmetic_progression(first_el, difference, count_numbers))

''' 
Задача 32: 
Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

max = int(input("Задайте максимальное значение: "))
min = int(input("Задайте минимально значение: "))

import random
array = [random.randint(1, 10) for _ in range(10)]
print(array)
index = []
for i in range(len(array)):
    if max > array[i] > min:
        index.append(i)
print(index)
