hour = int(input())

if hour == 12:
    print('Обедать')
elif (8 <= hour <= 11) or (13 <= hour <= 16):
    print('Работать')
else:
    print('Отдыхать')