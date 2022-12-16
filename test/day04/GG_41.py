import random


class Game:
    #类属性
    top_score =0
    def __init__(self,name):
        self.name=name

    def show_help(self):
        print("游戏的帮助信息")

    def show_top_score(self):
        print(f"游戏的最高分为：{Game.top_score}")

    def start_game(self):
        score = random.randint(10,100)
        print(f"本次游戏得分为{score}")
        if score>Game.top_score:
            Game.top_score=score


xw=Game("小伟")
xw.start_game()
xw.show_top_score()
xw.start_game()
xw.show_top_score()

