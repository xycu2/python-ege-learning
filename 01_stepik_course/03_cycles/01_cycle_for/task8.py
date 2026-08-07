num1 = int(input())
num2 = int(input())

minNum = num2

for i in range(num1, num2 + 1):

    if (i % 12 == 0) and (i % 14 == 0) and (i < minNum):
        minNum = i

print(minNum)