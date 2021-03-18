def sum_max(a, b, c, d, e):
    my_list = [a, b, c, d, e]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return
print(sum_max(100, 10, 1000, 1010, 1010010))


