while True:
    try:
        a = int(input('Введите радиус 1 круга и нажмите "Enter": '))
        break
    except ValueError:
        print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')

while True:
    try:
        b = int(input('Введите радиус 2 круга и нажмите "Enter": '))
        break
    except ValueError:
        print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')

c = 3.14*a*a
d = 3.14*b*b
k = c-d
l = d-c

if a>b:
    print('Круг 1 имеет большую площадь')
    print(f'Разность площадей круга = {k}')
else:
    print('Круг 2 имеет большую площадь')
    print(f'Разность площадей круга = {l}')