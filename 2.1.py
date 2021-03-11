my_list = [1, (-2 + -5), (2 - 0j), True, False, 6.3*2, [15, 12], {2, 1}, (8, 3, 1.1), {4: 'four', 5: 'five'}, {9, 10},
           range(11), b'two', bytearray(b'one'), ('a', 'b'), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")