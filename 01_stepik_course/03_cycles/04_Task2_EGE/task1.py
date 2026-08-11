print('a b c d')

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = (a <= d) and (not(b <= c))
                if f == 1:
                    print(a, b, c, d)