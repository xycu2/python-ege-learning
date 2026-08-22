point = input().split()

for i in range(len(point)):
    point[i] = int(point[i])

point.remove(max(point))
point.remove(min(point))

print(sum(point) / len(point))
