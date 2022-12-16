class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__被调用了")

    def __str__(self):
        return f'小猫名字{self.name},年龄是{self.age}'


# Cat("蓝猫","3")  # 创建对象
blue_cat = Cat("蓝猫", "3")  # 创建对象
blue = blue_cat  # 引用  ，没有创建对象
print(blue)
black_cat = Cat("黑猫", 10)
print(black_cat)
