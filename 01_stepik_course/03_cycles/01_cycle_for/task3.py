countStudent = int(input())
count = 0
summ = 0

for i in range(countStudent):
    num = int(input())
    summ += num
    count += 1

print(summ / count)