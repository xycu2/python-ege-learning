count = 0
for a1 in '1234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                number = a1 + a2 + a3 + a4
                if len(number) == len(set(number)):
                    if '26' not in number and '62' not in number:
                        count += 1

print(count)