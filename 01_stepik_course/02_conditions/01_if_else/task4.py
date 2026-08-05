num = int(input())

a = num % 10
num //= 10
b = num % 10

if a == b:
    print('Да')
else:
    print('Нет')