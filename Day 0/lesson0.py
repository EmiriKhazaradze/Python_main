from turtle import *


#we want to paint house

#step 1 draw a square
shape("turtle")

width(7)

color("orange")
begin_fill()
speed(30)


forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawind door

forward(70)
color("black")
begin_fill()
left(90)
forward(120) #height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(150,150)
pendown()
right(-30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)
color("orange")
left(90)
forward(50)
left(180)
forward(170)
right(90)
forward(200)
right(90)
forward(100)
right(90)
color("blue")
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(180)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(180)
forward(50)
right(90)
forward(25)
right(90)
forward(25)









exitonclick()