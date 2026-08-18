count = 0
for a1 in 'АРБУЗИК':
    for a2 in 'АРБУЗИК':
        for a3 in 'АРБУЗИК':
            for a4 in 'АРБУЗИК':
                for a5  in 'АРБУЗИК':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('А') + word.count('У') + word.count('И') <= 3:
                        count += 1

print(count)