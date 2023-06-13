import random

def game():

    print("欢迎来到恐怖大厦！")

    print("你现在在一间黑暗的房间里，你可以选择向左走、向右走或向前走。")

    direction = input("你想往哪个方向走？(左/右/前)")

    if direction == "左":

        print("你走进了一个鬼屋，里面有许多鬼魂在游荡。")

        action = input("你想逃跑、继续前进还是攻击鬼魂？(逃跑/前进/攻击)")

        if action == "逃跑":

            print("你成功逃脱了鬼屋，但是你的心理阴影面积增加了。")

        elif action == "前进":

            print("你勇敢地继续前进，发现了一个隐藏的房间。")

            choice = input("你想进入这个房间吗？(是/否)")

            if choice == "是":

                print("你进入了这个房间，发现了一本神秘的魔法书。")

                decision = input("你想拿起这本书吗？(是/否)")

                if decision == "是":

                    print("你拿起了这本书，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这股力量击败鬼魂吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了鬼魂，成为了这个鬼屋的主人。")

                    else:

                        print("你选择不使用这股力量，安静地离开了鬼屋。")

                else:

                    print("你选择不拿起这本书，安静地离开了鬼屋。")

            else:

                print("你选择不进入这个房间，安静地离开了鬼屋。")

        else:

            result = random.choice(["成功", "失败"])

            if result == "成功":

                print("你成功击败了鬼魂，成为了这个鬼屋的主人。")

            else:

                print("你攻击失败，被鬼魂抓住了。")

    elif direction == "右":

        print("你走进了一个墓地，里面有许多僵尸在游荡。")

        action = input("你想逃跑、继续前进还是攻击僵尸？(逃跑/前进/攻击)")

        if action == "逃跑":

            print("你成功逃脱了墓地，但是你的心理阴影面积增加了。")

        elif action == "前进":

            print("你勇敢地继续前进，发现了一个隐藏的地下室。")

            choice = input("你想进入这个地下室吗？(是/否)")

            if choice == "是":

                print("你进入了这个地下室，发现了一把神秘的剑。")

                decision = input("你想拿起这把剑吗？(是/否)")

                if decision == "是":

                    print("你拿起了这把剑，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这把剑击败僵尸吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了僵尸，成为了这个墓地的主人。")

                    else:

                        print("你选择不使用这把剑，安静地离开了墓地。")

                else:

                    print("你选择不拿起这把剑，安静地离开了墓地。")

            else:

                print("你选择不进入这个地下室，安静地离开了墓地。")

        else:

            result = random.choice(["成功", "失败"])

            if result == "成功":

                print("你成功击败了僵尸，成为了这个墓地的主人。")

            else:

                print("你攻击失败，被僵尸咬伤了。")

    else:

        print("你走进了一个森林，里面有许多野兽在游荡。")

        action = input("你想逃跑、继续前进还是攻击野兽？(逃跑/前进/攻击)")

        if action == "逃跑":

            print("你成功逃脱了森林，但是你的心理阴影面积增加了。")

        elif action == "前进":

            print("你勇敢地继续前进，发现了一个隐藏的山洞。")

            choice = input("你想进入这个山洞吗？(是/否)")

            if choice == "是":

                print("你进入了这个山洞，发现了一把神秘的弓箭。")

                decision = input("你想拿起这把弓箭吗？(是/否)")

                if decision == "是":

                    print("你拿起了这把弓箭，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这把弓箭击败野兽吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了野兽，成为了这个森林的主人。")

                    else:

                        print("你选择不使用这把弓箭，安静地离开了森林。")

                else:

                    print("你选择不拿起这把弓箭，安静地离开了森林。")

            else:

                print("你选择不进入这个山洞，安静地离开了森林。")

        else:

            result = random.choice(["成功", "失败"])

            if result == "成功":

                print("你成功击败了野兽，成为了这个森林的主人。")
                import random

def game():

    print("欢迎来到恐怖大厦！")

    print("你现在在一间黑暗的房间里，你可以选择向左走、向右走或向前走。")

    direction = input("你想往哪个方向走？(左/右/前)")

    if direction == "左":

        print("你走进了一个鬼屋，里面有许多鬼魂在游荡。")

        action = input("你想逃跑、继续前进还是攻击鬼魂？(逃跑/前进/攻击)")

        if action == "逃跑":

            print("你成功逃脱了鬼屋，但是你的心理阴影面积增加了。")

        elif action == "前进":

            print("你勇敢地继续前进，发现了一个隐藏的房间。")

            choice = input("你想进入这个房间吗？(是/否)")

            if choice == "是":

                print("你进入了这个房间，发现了一本神秘的魔法书。")

                decision = input("你想拿起这本书吗？(是/否)")

                if decision == "是":

                    print("你拿起了这本书，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这股力量击败鬼魂吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了鬼魂，成为了这个鬼屋的主人。")

                    else:

                        print("你选择不使用这股力量，安静地离开了鬼屋。")

                else:

                    print("你选择不拿起这本书，安静地离开了鬼屋。")

            else:

                print("你选择不进入这个房间，安静地离开了鬼屋。")

        else:

            result = random.choice(["成功", "失败"])

            if result == "成功":

                print("你成功击败了鬼魂，成为了这个鬼屋的主人。")

            else:

                print("你攻击失败，被鬼魂抓住了。")

    elif direction == "右":

        print("你走进了一个墓地，里面有许多僵尸在游荡。")

        action = input("你想逃跑、继续前进还是攻击僵尸？(逃跑/前进/攻击)")

        if action == "逃跑":

            print("你成功逃脱了墓地，但是你的心理阴影面积增加了。")

        elif action == "前进":

            print("你勇敢地继续前进，发现了一个隐藏的地下室。")

            choice = input("你想进入这个地下室吗？(是/否)")

            if choice == "是":

                print("你进入了这个地下室，发现了一把神秘的剑。")

                decision = input("你想拿起这把剑吗？(是/否)")

                if decision == "是":

                    print("你拿起了这把剑，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这把剑击败僵尸吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了僵尸，成为了这个墓地的主人。")

                    else:

                        print("你选择不使用这把剑，安静地离开了墓地。")

                else:

                    print("你选择不拿起这把剑，安静地离开了墓地。")

            else:

                print("你选择不进入这个地下室，安静地离开了墓地。")

        else:

            result = random.choice(["成功", "失败"])

            if result == "成功":

                print("你成功击败了僵尸，成为了这个墓地的主人。")

            else:

                print("你攻击失败，被僵尸咬伤了。")

    else:

        print("你走进了一个森林，里面有许多野兽在游荡。")

        action = input("你想逃跑、继续前进还是攻击野兽？(逃跑/前进/攻击)")

        if action == "逃跑":

            print("你成功逃脱了森林，但是你的心理阴影面积增加了。")

        elif action == "前进":

            print("你勇敢地继续前进，发现了一个隐藏的山洞。")

            choice = input("你想进入这个山洞吗？(是/否)")

            if choice == "是":

                print("你进入了这个山洞，发现了一把神秘的弓箭。")

                decision = input("你想拿起这把弓箭吗？(是/否)")

                if decision == "是":

                    print("你拿起了这把弓箭，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这把弓箭击败野兽吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了野兽，成为了这个森林的主人。")

                    else:

                        print("你选择不使用这把弓箭，安静地离开了森林。")

                else:

                    print("你选择不拿起这把弓箭，安静地离开了森林。")

            else:

                print("你选择不进入这个山洞，安静地离开了森林。")

        else:

            result = random.choice(["成功", "失败"])

            if result == "成功":

                print("你成功击败了野兽，成为了这个森林的主人。")

            else:

                print("你攻击失败，被野兽攻击了。")

game()

            else:

                print("你攻击失败，被野兽攻击了。")

game()
import random

def game():

    print("欢迎来到恐怖大厦！")

    print("你现在在一间黑暗的房间里，你可以选择向左走或向右走。")

    direction = input("你想往哪个方向走？(左/右)")

    if direction == "左":

        print("你走进了一个鬼屋，里面有许多鬼魂在游荡。")

        action = input("你想逃跑还是继续前进？(逃跑/前进)")

        if action == "逃跑":

            print("你成功逃脱了鬼屋，但是你的心理阴影面积增加了。")

        else:

            print("你勇敢地继续前进，发现了一个隐藏的房间。")

            choice = input("你想进入这个房间吗？(是/否)")

            if choice == "是":

                print("你进入了这个房间，发现了一本神秘的魔法书。")

                decision = input("你想拿起这本书吗？(是/否)")

                if decision == "是":

                    print("你拿起了这本书，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这股力量击败鬼魂吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了鬼魂，成为了这个鬼屋的主人。")

                    else:

                        print("你选择不使用这股力量，安静地离开了鬼屋。")

                else:

                    print("你选择不拿起这本书，安静地离开了鬼屋。")

            else:

                print("你选择不进入这个房间，安静地离开了鬼屋。")

    else:

        print("你走进了一个墓地，里面有许多僵尸在游荡。")

        action = input("你想逃跑还是继续前进？(逃跑/前进)")

        if action == "逃跑":

            print("你成功逃脱了墓地，但是你的心理阴影面积增加了。")

        else:

            print("你勇敢地继续前进，发现了一个隐藏的地下室。")

            choice = input("你想进入这个地下室吗？(是/否)")

            if choice == "是":

                print("你进入了这个地下室，发现了一把神秘的剑。")

                decision = input("你想拿起这把剑吗？(是/否)")

                if decision == "是":

                    print("你拿起了这把剑，突然感觉到一股强大的力量涌入你的身体。")

                    final_choice = input("你想使用这把剑击败僵尸吗？(是/否)")

                    if final_choice == "是":

                        print("你成功击败了僵尸，成为了这个墓地的主人。")

                    else:

                        print("你选择不使用这把剑，安静地离开了墓地。")

                else:

                    print("你选择不拿起这把剑，安静地离开了墓地。")

            else:

                print("你选择不进入这个地下室，安静地离开了墓地。")

game()
