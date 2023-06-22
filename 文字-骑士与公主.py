import random

def game():

    print("欢迎来到这个古代王国。你是一个勇敢的骑士，你的名字叫做亚瑟。你一直暗恋着美丽的公主莉莉。")

    print("但是，一天，公主被恶龙掳走了。国王悬赏重金，希望有人能够拯救公主。")

    print("你决定踏上这场冒险，拯救公主并赢得她的芳心。")

    print("在你的旅途中，你遇到了国王和王后。他们为你提供了帮助，并给了你一些宝贵的建议。")

    print("你也遇到了其他骑士，他们也在寻找公主。你可以选择与他们合作，也可以选择独自行动。")

    print("最终，你来到了恶龙的洞穴，准备与它决一死战。")

    while True:

        choice = input("你会怎么做？A.攻击 B.防御 C.使用魔法 D.使用道具 E.请求帮助 F.逃跑 ")

        if choice == "A":

            attack = random.randint(1, 10)

            if attack > 5:

                print("你成功击败了恶龙，拯救了公主！")

                break

            else:

                print("你被恶龙击中，损失了一些生命值。")

        elif choice == "B":

            defense = random.randint(1, 10)

            if defense > 7:

                print("你成功防御了恶龙的攻击。")

            else:

                print("你被恶龙击中，损失了一些生命值。")

        elif choice == "C":

            magic = random.randint(1, 10)

            if magic > 8:

                print("你使用魔法攻击恶龙，造成了巨大的伤害！")

            else:

                print("你使用魔法失败，损失了一些魔力值。")

        elif choice == "D":

            item = random.randint(1, 10)

            if item > 6:

                print("你使用道具攻击恶龙，造成了巨大的伤害！")

            else:

                print("你使用道具失败，没有造成任何伤害。")

        elif choice == "E":

            help = random.randint(1, 10)

            if help > 4:

                print("其他骑士来帮助你，一起攻击恶龙！")

            else:

                print("其他骑士没有及时赶到，你必须独自面对恶龙。")

        elif choice == "F":

            print("你逃跑了，但公主仍然被困在恶龙的洞穴里。")

            break

        else:

            print("无效输入，请重新选择。")

game()
