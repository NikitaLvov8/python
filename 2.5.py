rating = [1, 2, 3, 4, 5]
for _ in range(10):
    a = int(input("Введите число: "))
    flag = False
    for b in range(len(rating)):
        if rating[b] < a:
            rating.insert(b, a)
            flag = True
            break
    if not flag:
        rating.append(a)
    print(*rating)
