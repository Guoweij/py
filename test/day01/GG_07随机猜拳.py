import random

bet = int(input("石头为1，剪刀为2，布为3,输入一个"))   # str转int
computer = random.randint(1, 3)
if (bet == 1 and computer == 2) or (bet == 2 and computer == 3) or (bet == 3 and computer == 1):
    print("赢了")
elif bet == computer:
    print("平局")
else:
    print("GG输了")
