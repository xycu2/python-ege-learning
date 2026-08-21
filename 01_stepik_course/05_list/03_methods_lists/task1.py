listMax = []

for i in range(7):
    points = int(input())
    listMax.append(points)

listMax.sort(reverse=True)

print(sum(listMax[:4]))

