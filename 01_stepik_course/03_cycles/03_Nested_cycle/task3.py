# 11x+20y=1000
total_sum = 0

# Перебираем x и y в разумных границах:
# Так как 11x < 1000, то x максимум около 90
# Так как 20y < 1000, то y максимум около 50

for x in range(1, 100):
    for y in range(1, 100):
        if 11 * x + 20 * y == 1000:
            total_sum += x + y

print(total_sum)
