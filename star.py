from turtle import *
shape("turtle")
speed(10)
color('darkgreen', 'orange')
begin_fill()
while True:
    forward(50)
    left(140)
    if abs(pos()) < 1:
        break
end_fill()
write("May the force be with you!", align="right")
exitonclick()