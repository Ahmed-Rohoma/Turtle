from turtle import Turtle, Screen
from Turtle import Player
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_turtle = screen.textinput(title="Color Choice",
                               prompt="Enter Your Turtle Color :")
color = ["red", "blue", "green", "orange", "purple", "yellow"]
all_turtle = []


def random_num():
    return randint(0, 10)


race_on = False
for i in range(6):
    x = Player(color[i], "turtle")
    all_turtle.append(x)
if user_turtle:
    race_on = True
while race_on:
    for turtle in all_turtle:
        if turtle.tim.xcor() > 210:
            race_on = False
            if turtle.tim.pencolor() == user_turtle:
                print(f"You've The Winner ,{user_turtle} Turtle won .")
            else:
                print(f"You've lost ,{turtle.tim.pencolor()} Turtle won .")
        turtle.tim.forward(random_num())
    

screen.exitonclick()
