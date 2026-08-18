count = 0
for a1 in 'ШКОЛА':
    for a2 in 'ШКОЛА':
        for a3 in 'ШКОЛА':
            for a4 in 'ШКОЛА':
                for a5 in 'ШКОЛА':
                    for a6 in 'ШКОЛА':
                        word = a1 + a2 + a3 + a4 + a5 + a6

                        # Заменяем все гласные буквы на Г
                        temp = word.replace('А', 'Г').replace('О','Г')

                        if 'ГГ' not in temp:
                            count += 1

print(count)