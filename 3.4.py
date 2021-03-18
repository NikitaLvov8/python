def my_func(x, y):
    return 1 \
        if y == 0 \
        else my_func (x, y + 1) * 1 / x
print(round(my_func(int(input('Введите действительный положительный х: ')), int(input('Введите целый отрицательный у: ')), 10)))
