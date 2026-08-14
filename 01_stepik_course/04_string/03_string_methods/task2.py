a = input('')
s = a.index('l')
b = a[s::]

b = b.replace('l', '', 1)
print(b)