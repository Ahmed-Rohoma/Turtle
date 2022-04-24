from turtle import Turtle


class Player:
    player_num = 0

    def __init__(self, color, shape):
        Player.player_num += 1
        self.tim = Turtle(shape=shape)
        self.tim.color(color)
        self.tim.penup()
        self.tim.goto(-240, -170 + 50*Player.player_num)

