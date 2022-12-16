def num1(*args, **kwargs):
    num = 0
    for i in args:
        num = num + i
    for j in kwargs.values():
        num = num + j
    print(num)


num1(1, 2, 3, 5, c=12, d=30)
