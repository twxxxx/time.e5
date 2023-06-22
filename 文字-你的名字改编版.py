import random

def start_game():

print("欢迎来到《你的名字》文字游戏！")

print("在这个游戏中，你将扮演电影中的主人公，体验他们的故事。")

print("游戏开始！")

first_choice()

def first_choice():

print("你是一个高中生，名叫立花泷。你住在东京，每天都过着忙碌的生活。")

print("今天，你突然发现自己身处一个陌生的地方，周围都是山林和稻田。")

print("你感到非常困惑，不知道自己为什么会在这里。")

choice = input("你决定：1.四处走走，看看周围的环境 2.呆在原地，等待救援 ")

if choice == "1":

explore()

else:

wait_for_rescue()

def explore():

print("你四处走走，发现自己身处一个叫做糸守町的小镇。")

print("镇上的人们都很友善，他们告诉你这里是长野县的一个小镇。")

print("你感到非常惊讶，不知道自己是怎么来到这里的。")

choice = input("你决定：1.继续探索小镇 2.打电话给家人求助 ")

if choice == "1":

keep_exploring()

else:

call_family()

def keep_exploring():

print("你继续在小镇上走动，发现这里有一个美丽的神社。")

print("神社里有一个少女在祈祷，她看起来非常认真。")

print("你感到好奇，想要过去看看。")

choice = input("你决定：1.走过去和少女交谈 2.离开神社 ")

if choice == "1":

talk_to_girl()

else:

leave_shrine()

def talk_to_girl():

print("你走过去和少女交谈，发现她叫三叶。")

print("三叶告诉你她是镇上神社的巫女，每天都会在这里祈祷。")

print("你和三叶聊了很久，发现她是一个非常善良、温柔的女孩。")

choice = input("你决定：1.继续和三叶交谈 2.离开神社 ")

if choice == "1":

keep_talking_to_girl()

else:

leave_shrine()

def keep_talking_to_girl():

print("你和三叶继续聊天，发现她对自己所在的小镇非常热爱。")

print("她希望能够为小镇做些贡献，让更多人了解这里的美好。")

print("你被三叶的热情所感染，也想为小镇做些事情。")

choice = input("你决定：1.帮助三叶宣传小镇 2.离开神社 ")

if choice == "1":

help_girl()

else:

leave_shrine()

def help_girl():

print("你决定帮助三叶宣传小镇，让更多人了解这里的美好。")

print("你和三叶一起在小镇上发传单，向游客介绍小镇的风景和文化。")

print("经过你们的努力，越来越多的人开始关注这个小镇。")

print("三叶非常感谢你的帮助，你们成为了好朋友。")

end_game()

def wait_for_rescue():

print("你决定呆在原地等待救援。")

print("过了一会儿，一个警察走了过来。")

print("他告诉你，你昏迷了一段时间，被人发现后送到了医院。")

print("你感到非常惊讶，不知道自己为什么会昏迷。")

choice = input("你决定：1.跟随警察离开 2.留在原地继续等待 ")

if choice == "1":

follow_cop()

else:

keep_waiting()

def follow_cop():

print("你跟随警察离开了原地。")

print("警察带你去了医院，让医生给你做了一个检查。")

print("医生告诉你，你的身体状况良好，没有任何问题。")

print("你感到非常困惑，不知道自己为什么会昏迷。")

choice = input("你决定：1.离开医院 2.留在医院观察 ")

if choice == "1":

leave_hospital()

else:

stay_in_hospital()

def leave_hospital():

print("你决定离开医院。")

print("当你走出医院的时候，突然发现自己又回到了东京。")

print("你感到非常惊讶，不知道自己是怎么回来的。")

choice = input("你决定：1.回家 2.四处走走 ")

if choice == "1":

go_home()

else:

wander_around()

def go_home():

print("你决定回家。")

print("当你走进家门的时候，发现家里的一切都和往常一样。")

print("你的父母和妹妹都在家里，他们看起来并没有发现什么异常。")

print("你感到非常困惑，不知道自己究竟经历了什么。")

end_game()

def wander_around():

print("你决定四处走走。")

print("当你走在东京的街头时，突然发现自己又回到了糸守町。")

print("你感到非常惊讶，不知道自己为什么会突然回到这里。")

choice = input("你决定：1.继续探索小镇 2.呆在原地等待救援 ")

if choice == "1":

explore()

else:

wait_for_rescue()

def leave_shrine():

print("你决定离开神社。")

print("当你走出神社的时候，突然发现自己又回到了东京。")

print("你感到非常惊讶，不知道自己是怎么回来的。")

choice = input("你决定：1.回家 2.四处走走 ")

if choice == "1":

go_home()

else:

wander_around()

def call_family():

print("你拿出手机，准备给家人打电话求助。")

print("但是当你拨通电话的时候，却发现对方无法听到你的声音。")

print("你感到非常绝望，不知道该怎么办。")

choice = input("你决定：1.继续尝试打电话 2.放弃打电话，继续探索小镇 ")

if choice == "1":

keep_calling()

else:

explore()

def keep_calling():

print("你继续尝试打电话，但是始终无法接通。")

print("你感到非常沮丧，不知道自己该怎么办。")

choice = input("你决定：1.放弃打电话，继续探索小镇 2.呆在原地等待救援 ")

if choice == "1":

explore()

else:

wait_for_rescue()

def stay_in_hospital():

print("你决定留在医院观察。")

print("医生每天都会来检查你的身体状况，确保你没有任何问题。")

print("过了几天，你的身体状况一直都很稳定。")

print("医生告诉你，你可以出院了。")

choice = input("你决定：1.离开医院 2.再留几天 ")

if choice == "1":

leave_hospital()

else:

stay_in_hospital()

def keep_waiting():

print("你决定继续等待救援。")

print("过了一会儿，一个救护车来到了你的身边。")

print("医护人员把你抬上救护车，送往医院。")

print("在医院里，医生给你做了一个全面的检查。")

print("他们告诉你，你的身体状况良好，没有任何问题。")

end_game()

def end_game():

print("游戏结束！感谢您的参与！")

start_game()
