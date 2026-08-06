# 1
number = int(input())

num1 = number % 10

number //= 10
num2 = number % 10

number //= 10
num3 = number % 10

num4 = number // 10

if (num1 == num4) and (num2 == num3):
    print('YES')
else:
    print('NO')

#  2
s = input()

if s == s[::-1]:
    print('YES')
else:
    print('NO')