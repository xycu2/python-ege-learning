mult = 1

num = int(input())
mult *= num % 10
num //= 10
mult *= num % 10
num //= 10
mult *= num % 10
print(mult)
