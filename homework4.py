print('Подсчет уравнения по формуле x=(a*b*b)/c')
print('Введите число a')
a = input()
print('Введите число b')
b = input()
print('Введите число c')
c = input()

if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)

    if c == 0:
        print('c не может равняться 0 для выполнения деления.')
    else:
        x = (a * b * b) / c
        print(f'Полученный результат: {x}')
else:
    print('Неверно, вводите целые числа для подсчета уравнения')