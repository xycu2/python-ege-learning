n = int(input())
summ = 0

for i in range(n):
    string = input()

    if string == string[::-1]:
        summ += 1

print(summ)