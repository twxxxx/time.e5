import turtle
import datetime

def draw_clock():
    # 绘制表盘
    turtle.pensize(7)
    for i in range(60):
        if i % 5 == 0:
            turtle.penup()
            turtle.forward(200)
            turtle.pendown()
            turtle.forward(20)
            turtle.penup()
            turtle.backward(220)
        else:
            turtle.penup()
            turtle.forward(210)
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.backward(220)
        turtle.right(6)

    # 绘制时针
    hour = datetime.datetime.now().hour % 12
    minute = datetime.datetime.now().minute
    angle = (hour * 60 + minute) / 720 * 360
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    turtle.right(angle)
    turtle.pendown()
    turtle.forward(100)

    # 绘制分针
    angle = minute / 60 * 360
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    turtle.right(angle)
    turtle.pendown()
    turtle.forward(180)

def main():
    # 初始化turtle窗口
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=600, height=600)

    # 绘制表盘和指针
    draw_clock()

    # 隐藏turtle画笔
    turtle.hideturtle()

if __name__ == '__main__':
    main()
