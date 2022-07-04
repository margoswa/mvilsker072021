from turtle import *
shape("turtle")
speed(10)
color('darkgreen', 'orange')
begin_fill()
while True:
    forward(250)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

backward(100)
write("May the force be with you!", align="right")
exitonclick()