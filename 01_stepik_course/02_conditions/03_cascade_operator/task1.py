age = int(input())

if age < 18:
    print('Чай')
elif 18 <= age <= 60:
    print('Вино')
else:
    print('Морс')