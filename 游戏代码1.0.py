import random

# 初始化游戏变量
word = "铃芽户缔"
lives = 3
current_round = 1

# 生成地点列表
locations = [
    (1, 1),
    (2, 1),
    (3, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (1, 3),
    (2, 3),
    (3, 3),
    (1, 4),
    (2, 4),
    (3, 4),
    (4, 4)
]

# 生成随机动作列表
actions = [
    (1, "前进1步"),
    (2, "前进2步"),
    (3, "前进3步"),
    (4, "前进4步"),
    (5, "原地不动"),
    (6, "向左1步"),
    (7, "向左2步"),
    (8, "向左3步"),
    (9, "向右1步"),
    (10, "向右2步"),
    (11, "向右3步"),
    (12, "向上1步"),
    (13, "向上2步"),
    (14, "向上3步"),
    (15, "向下1步"),
    (16, "向下2步"),
    (17, "向下3步")
]

# 开始游戏
while True:
    print(f"第{current_round}局，{word}")
    print("1. 前进")
    print("2. 后退")
    print("3. 原地不动")
    print("4. 攻击")
    print("5. 防御")
    print("6. 跳跃")
    print("7. 使用道具")
    print("8. 退出游戏")

    # 模拟玩家操作
    action = input("请输入您的操作（1-退出，2-攻击，3-防御，4-跳跃，5-使用道具）：")
    if action == "1":
        print("前进{lives}步")
        current_round += 1
    elif action == "2":
        print("后退{lives}步")
        current_round -= 1
    elif action == "3":
        print("原地不动")
    elif action == "4":
        print(f"攻击{locations[random.randint(0, 4)]}，造成{random.randint(10, 50)}点伤害")
    elif action == "5":
        print(f"防御{locations[random.randint(0, 4)]}次，抵御了{random.randint(10, 50)}点伤害")
    elif action == "6":
        print("跳跃至{locations[random.randint(0, 4)]}米高")
    elif action == "7":
        print("使用道具{random.choice(actions[:4])}")
    elif action == "8":
        print("游戏结束")
        break
    elif action == "4" or action == "5":
        print("{word}发动了一次攻击，命中了{locations[random.randint(0, 4)]}，造成{random.randint(10, 50)}点伤害。"
            "还剩{lives}条命，{current_round}局。")
    elif action == "3":
        print("{word}站在原地，不动了。"
            "还剩{lives}条命，{current_round}局。")
    elif action == "2":
        print("{word}向后退{lives}步。"
            "还剩{lives}条命，{current_round}局。")
    elif action == "1":
        print("{word}向前进{lives}步。"
            "还剩{lives}条命，{current_round}局。")

    # 判断是否游戏结束
    if word == "铃芽户缔":
        print("恭喜{word}，你赢了！")
        break

    # 给予玩家一些提示
    elif current_round == 5:
        print("第5局，要小心了！")
    elif current_round == 10:
        print("第10局，你已经很强了！")
    elif current_round == 20:
        print("第20局，你是最强的！")
    elif current_round == 30:
        print("第30局，你已经无敌了！")
    elif current_round > 30:
        print("第{round}局，你已经是传说中的{word}！")

    # 给予玩家一些奖励
    elif round_num > 1 and round_num % 5 == 0:
        print("第{round}局，你获得了{word}的专属道具！")
    elif round_num > 1 and round_num % 5 == 1:
        print("第{round}局，你获得了{word}的高级道具！")
    elif round_num > 1 and round_num % 5 == 2:
        print("第{round}局，你获得了{word}的特级道具！")
    elif round_num > 1 and round_num % 5 == 3:
        print("第{round}局，你获得了{word}的顶级道具！")
    elif round_num > 1 and round_num % 5 == 4:
        print("第{round}局，你获得了{word}的神级道具！")

    # 给予玩家一些惩罚
    elif round_num > 20 and round_num % 5 != 0:
        print("第{round}局，你受到了惩罚，生命值减少了{random.randint(50, 100)}点！")
    elif round_
