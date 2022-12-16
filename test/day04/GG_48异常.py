try:
    num = input("打数字")
    num = int(num)
    print(num)
    a = 10 / num
    print(f'a:{a}')

except Exception as e:
    print(f"错误信息为：{e}")
else:
    print("没问题")
finally:
    print("真不错")
