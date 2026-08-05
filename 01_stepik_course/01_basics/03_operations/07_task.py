# 1
newNum = ''
num = int(input())

newNum += str(num % 10)
num //= 10
newNum += str(num % 10)
num //= 10
newNum += str(num % 10)
num //= 10
newNum += str(num % 10)
num //= 10
print(newNum)


# 2
x = int( input())
a = x % 10
b = (x % 100) // 10
c = (x // 100) % 10
d = x // 1000
print( a, b, c, d, sep= "" )