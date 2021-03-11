i = input('Введите слова через пробел: ').split()
for a, word in enumerate(i):
    print(a, word)\
        if len(word) <= 10 else print(a, word[:10])

