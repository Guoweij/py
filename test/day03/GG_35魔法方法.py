class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__被调用了")

    def show_info(self):
        print(f"猫的名字：{self.name},猫的年龄：{self.age}")


# Cat("蓝猫","3")  # 创建对象
blue_cat = Cat("蓝猫", "3")  # 创建对象
blue = blue_cat  # 引用  ，没有创建对象
blue.show_info()

black_cat = Cat("黑猫", 10)
black_cat.show_info()
