def div(i, x):
    try:
        return int(i) / int(x)
    except ZeroDivisionError:
        print('Division by zero is forbidden')
    except ValueError:
        print('You should enter integers')
print(div(input(), input()))