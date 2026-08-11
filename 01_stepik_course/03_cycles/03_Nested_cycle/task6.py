count = 0

for one in range(10):
    for two in range(10):
        for three in range(10):
            for four in range(10):
                if (one == two) and (three == four):
                    count += 1
print(count)