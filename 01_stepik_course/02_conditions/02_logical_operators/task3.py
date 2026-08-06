number = int(input())

num1 = number % 10

number //= 10
num2 = number % 10

number //= 10
num3 = number % 10

num4 = number // 10

if ((num1 != num2) and (num2 != num3) and
    (num3 != num4) and (num1 != num4) and
    (num1 != num3) and (num2 != num4)):
    print('YES')
else:
    print('NO')