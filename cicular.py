from turtle import *
from colorsys import *
bgcolor('Dark Blue')
pensize (5)
h = 1.0
tracer (4)
up()
goto(-240, 90)
down()
for i in range(360):
    c = hsv_to_rgb(h, 1,1)
    color(c)
    h+=0.005
    for j in range(5):
        fd(100)
        lt(5)
        lt(65)
        circle(250)
        lt(65)
        circle(250)
        lt(65)
        done()
