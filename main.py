from turtle import *

speed(2)

# Program 1

# forward(200)

# Program 2

# forward(200)
# right(90)
# forward(100)
# right(90)
# forward(200)
# right(90)
# forward(100)

# Program 3

# blå bakgrund
fillcolor("blue")
color("blue")

begin_fill()
forward(300)
right(90)
forward(150)
right(90)
forward(300)
right(90)
forward(150)
end_fill()

# förflyttar sköldpaddan
right(90)
penup()
forward(60)
pendown()

# gul vertikal linje
fillcolor("yellow")
color("yellow")
begin_fill()
forward(30)
right(90)
forward(150)
right(90)
forward(30)
right(90)
forward(150)
end_fill()

# förflytta sköldpaddan
penup()
left(90)
forward(60)
left(90)
forward(60)

# horisontell gul linjen
left(90)
pendown()
begin_fill()
forward(300)
right(90)
forward(30)
right(90)
forward(300)
right(90)
forward(30)
end_fill()

done()