class GG:
    def __init__(self, name):
        self.name = name
        print(f"死亡笔记上写的名字是：{self.name}")

    def __del__(self):
        print(f"{self.name}他已经G了")


GG("张三")
