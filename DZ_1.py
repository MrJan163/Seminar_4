# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.



numbers = int(input('Введите размер списка: '))
list = []
sum_nechet = 0
for el in range(numbers):
    list_number = int(input(f'Введите число: {el + 1} '))
    list.append(list_number)
    if el % 2 != 0:
        sum_nechet += list[el]


print(list)
print(f'Сумма нечетных чисел равна: {sum_nechet}')