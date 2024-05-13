from turtle import *

width(20)
bgcolor("black")
position = [(0, 0), (-5, 13), (-5, 5)]
colors = ["#bd0f3c", "#50ebe7", "white"]

for (x, y), col in zip(position, colors):
    up()
    goto(x, y)
    down()
    color(col)
    left(180)
    circle(50, 270)
    forward(120)
    left(180)
    circle(50, 90)