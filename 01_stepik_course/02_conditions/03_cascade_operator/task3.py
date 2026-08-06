num1 = int(input())
num2 = int(input())
num3 = int(input())

count = (num1 > 0) + (num2 > 0) + (num3 > 0)

if count == 3:
    print(num1 * 2)
    print(num2 * 2)
    print(num3 * 2)
elif count == 2:
    print(num1 * 3)
    print(num2 * 3)
    print(num3 * 3)
elif count == 1:
    print(num1 ** 2)
    print(num2 ** 2)
    print(num3 ** 2)