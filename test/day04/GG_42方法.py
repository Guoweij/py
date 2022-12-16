import random


class Game:
    # 类属性
    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help(self):
        print("游戏的帮助信息")

    @classmethod
    def show_top_score(cls):
        print(f"游戏的最高分为：{cls.top_score}")

    def start_game(self):
        print(f"{self.name}开始游戏，游戏中……",end="")
        score = random.randint(10, 100)
        print(f"本次游戏得分为{score}")
        if score > Game.top_score:
            Game.top_score = score


xw = Game("小伟")
xw.start_game()
xw.show_top_score()
xw.start_game()
xw.show_top_score()
