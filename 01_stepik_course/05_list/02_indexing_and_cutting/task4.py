n = int(input())

shop1 = []

for _ in range(n):
    shop1.append(int(input()))

shop2 = []

for _ in range(n):
    shop2.append(int(input()))

result = []

for i in range(n):
    if shop1[i] < shop2[i]:
        result.append(shop1[i])
    else:
        result.append(shop2[i])

print(*result)