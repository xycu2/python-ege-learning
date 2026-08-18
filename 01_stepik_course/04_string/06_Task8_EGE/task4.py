count = 0
for a1 in 'ДИОНС':
    for a2 in 'ДИОНС':
        for a3 in 'ДИОНС':
            for a4 in 'ДИОНС':
                for a5 in 'ДИОНС':
                        word = a1 + a2 + a3 + a4 + a5

                        if word.count('Д') + word.count('Н') + word.count('С') < 3:
                            count += 1

print(count)