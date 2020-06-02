"""
    绘制分型树
"""
import turtle

def draw_branch(branch_length, level):
    if branch_length > 5:
        if level >= 6:
            turtle.pencolor("green")
            turtle.pensize(1)
        #绘制右侧

        turtle.pensize(3)
        turtle.forward(branch_length)
        print("forward", branch_length)
        turtle.right(20)
        print("right", 20)
        draw_branch(branch_length - 15, level + 1)
        #绘制左侧
        turtle.left(40)
        print("left", 40)
        draw_branch(branch_length - 15, level + 1)

        turtle.right(20)
        print("right", 20)
        turtle.backward(branch_length)
        print("backward", branch_length)

def main():
    """
        主函数
    :return:
    """

    turtle.left(90)

    turtle.penup()
    turtle.backward(150)
    turtle.pendown()


    draw_branch(100, 1)
    turtle.exitonclick()

if __name__ == "__main__":
    main()
