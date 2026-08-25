import fnmatch

for num in range(6718, 10 ** 9 + 1, 6718):
    if fnmatch.fnmatch(str(num), '?46?44*2'):
        print(num, num // 6718)

# 146244142 21769
# 146344912 21784
# 246644652 36714
# 346944392 51644