text = input().split()

maxLen = 0
maxWord = ''
for word in text:
    clean_word = word.strip(",.?!:;")

    if len(clean_word) > maxLen:
        maxLen = len(clean_word)
        maxWord = clean_word

print(maxWord)