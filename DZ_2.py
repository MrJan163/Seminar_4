# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)


import random
x = int(input('Введите координаты х: '))
y = int(input('Введите координаты y: '))

table = []
avg_lines = []
for el in range(y):
    table.append(list())
    s_a = 0
    for j in range(x):
        table[el].append(random.randint(0, 10))
        s_a += table[el][j]
    avg_lines.append(s_a // x)
    print(f'{table[el]} - average is {avg_lines[el]}')