from turtle import *
color('red', 'purple')
begin_fill()
while True:
    forward(200)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()