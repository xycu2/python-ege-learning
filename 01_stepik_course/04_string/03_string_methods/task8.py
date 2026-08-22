books = input().split()
nameBook = input()

if books.count(nameBook) > 0:
    print(books.index(nameBook))
else:
    print(-1)
