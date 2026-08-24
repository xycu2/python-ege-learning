def f(n):
    if n < 22:
        return 111

    if n >= 22 and n % 2 == 0:
        return  n + 7 * f(n - 3)

    if n >= 22 and n % 2 != 0:
        return 5 * f(n - 1)

s = str(f(35) + f(11))
mult = 1

for num in s:
    if int(num) != 0:
        mult *= int(num)

print(mult)