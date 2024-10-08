while True:
    try:
        a = int(input('Введите 1 число и нажмите "Enter": '))
        break
    except ValueError:
        print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')

while True:
    try:
        b = int(input('Введите 2 число и нажмите "Enter": '))
        break
    except ValueError:
        print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')

print(a + b)
print(a - b)
print(a * b)
print((a + b) / 2)

if a>0 and b>0 and a>b:
    print(a-b)
elif a>0 and b>0 and a<b:
    print(b-a)
elif a>0 and b<0:
    b1=b*(-1)
    if a>b1:
        print(a-b1)
    else:
        print(b1-a)
elif a<0 and b>0:
    a1 = a*(-1)
    if a1>b:
        print(a1-b)
    else:
        print(b-a1)
elif a<0 and b<0:
    a2=a*(-1)
    b2=b*(-1)
    if a2>b2:
        print(a2-b2)
    else:
        print(b2-a2)