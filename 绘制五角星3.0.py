"""
    作者：周润发
    功能：五角星绘制
    版本：1.0
    日期：20200601
    版本2.0：不同大小的五角星
    版本3.0：函数与循环结合，递归函数
"""


import turtle

def painting(BIAN):
    """
        绘制五角星函数
    :param BIAN:
    :return:
    """
    count = 1
    while count <= 5:
        turtle.forward(BIAN)
        turtle.right(144)
        count += 1

def draw_pentagram(BIAN):
    count = 1
    while count <= 5:
        turtle.forward(BIAN)
        turtle.right(144)
        count += 1

    #更新参数，迭代绘制，不在主函数里面更新
    BIAN += 10
    if BIAN <= 100:
        draw_pentagram(BIAN)


def main():
    """

    :return:
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')



    BIAN = 50
    draw_pentagram(BIAN)
    # while BIAN <= 500:
    #     painting(BIAN)
    #     BIAN += 10
    turtle.exitonclick()

if __name__ == "__main__":
    main()