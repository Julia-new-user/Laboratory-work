while True:
      try:
            imya = str(input('Введите Ваше имя: '))
            break
      except ValueError:
            print('Ошибка ввода. Убедитесь, что Вы вводите и попробуйте еще раз.')
while True:
      try:
            voz = int(input('Введите Ваш возраст: '))
            break
      except ValueError:
            print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')
while True:
      try:
            nom  = int(input('Введите номер школы: '))
            break
      except ValueError:
            print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')
while True:
      try:
            cl  = int(input('Введите номер класса: '))
            break
      except ValueError:
            print('Ошибка ввода. Убедитесь, что Вы вводите натуральное число и попробуйте еще раз.')

if cl==11:
      god = 2024-voz+18
elif cl==10:
      god = 2024-voz+17
elif cl==9:
      god = 2024-voz+16
elif cl==8:
      god = 2024-voz+15
elif cl==7:
      god = 2024-voz+14
elif cl==6:
      god = 2024-voz+13
elif cl==5:
      god = 2024-voz+12
elif cl==4:
      god = 2024-voz+11
elif cl==3:
      god = 2024-voz+10
elif cl==2:
      god = 2024-voz+9
elif cl==1:
      god = 2024-voz+8
print(f'''Привет, {imya}!
Поздравляю тебя с окончанием {cl} класса школы номер {nom}  в {god} году''')


