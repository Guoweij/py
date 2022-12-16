score = int(input("输入分数："))
if score >= 90:
    print("优")
elif score >= 80 and score < 90:
    # 有波浪线是怕写的人不知道优先级 建议用（）
    print("良")
elif score >= 70: # and score < 80:
    # and score < 80可以不写  因为上边判断了只有小于80的才会跳转到这一部判断
    print("中")
elif score >= 60: # and score < 70:
    print("差")
elif score < 60:
    print("不及格")
