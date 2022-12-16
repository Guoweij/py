list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
dict1 = {'a': 1, 'b': 5, "c": 6}

def num1(*args, **kwargs):
    num = 0
    for i in args:
        num = num + i
    for j in kwargs.values():
        num = num + j
    print(num)

num1(*list1,**dict1)