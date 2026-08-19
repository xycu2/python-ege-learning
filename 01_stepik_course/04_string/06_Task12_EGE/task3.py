max_len_str = 0
for n in range(6, 1000):
    s = '57' * n

    while '575' in s or '7777' in s:

        if '575' in s:
            s = s.replace('575', '77', 1)

        if '7777' in s:
            s = s.replace('7777', '5', 1)


    len_str = len(s)

    if len_str > max_len_str:
        max_len_str = len_str

print(max_len_str)