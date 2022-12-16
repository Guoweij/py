class human:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    def eat(self):
        self.weight += 1
        print("狂暴进食，胖了一斤")

    def run(self):
        self.weight -= 0.5
        print("猪突猛进，瘦了半斤")

    def __str__(self):
        return f"人物名称：{self.name},体重：{self.weight}kg"


xm = human("YYQ", 50)
print(xm)
xm.eat()
print(xm)
xm.run()
print(xm)
