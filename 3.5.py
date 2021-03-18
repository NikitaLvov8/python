num = 0
try:
    while True:
        for a in map(int, input('Введите числа с пробелом: ').split()):
            num += a
        print(num)
except ValueError:
    print(num)