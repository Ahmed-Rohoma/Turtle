from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def counter_clockwise():
    tim.left(20)


def with_clockwise():
    tim.right(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=with_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
