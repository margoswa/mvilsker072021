from turtle import *
shape("turtle")
speed(10)
color('darkgreen', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()