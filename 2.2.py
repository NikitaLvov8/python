my_list = input('Последовательно введите числа от 0 до 10: - ').split()
for a in range(1, len(my_list), 2):
    my_list[a - 1], my_list[a] = my_list[a], my_list[a - 1]
print(my_list)