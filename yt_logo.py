from turtle import *
bgcolor("black")
speed(10)
hideturtle()
width(4)
penup()
goto(160, -100)
pendown()
begin_fill()
color("#FF0000")
fillcolor("#FF0000")
left(90)
for i in range(2):
    forward(100)
    circle(50, 90)
    forward(200)
    circle(50, 90)
end_fill()
goto(-20, 0)
begin_fill()
color("#fff")
fillcolor("#fff")
left(180)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()

done()















