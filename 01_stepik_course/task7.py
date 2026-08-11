count = 0

for one in range(10):
    for two in range(10):
        for three in range(10):
            for four in range(10):
                if ((one % 2) + (two % 2) + (three % 2) + (four % 2)) == 2:
                    count += 1

print(count)
