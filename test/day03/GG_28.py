def calc(a, b):
    num1 = a + b
    num2 = a - b
    return num1, num2


result = calc(10, 5)
print(result, result[0], result[1])

x, y = calc(10, 5)
print(x, y)
