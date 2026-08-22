n = int(input())

ages = []

for _ in range(n):
    ages.append(int(input()))

ages.sort()

max_count = 0
ans_age = ages[0]

for age in ages:
    cnt = ages.count(age)

    if cnt > max_count:
        max_count = cnt
        ans_age = age

print(ans_age)