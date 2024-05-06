from turtle import *


#we want to paint a house

shape("turtle")
width(3)

speed(4)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#drawing a door


forward(70)
color("silver")
begin_fill()
left(90)

forward(120)
right(90)

forward(70)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()
 
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

color("black")

left(30)
forward(60)

left(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(30)

right(90)
forward(50)

right(180)
forward(25)

left(90)
forward(30)

#window2


penup()
goto(200, 200)
pendown()

forward(60)

right(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(30)

left(90)
forward(50)

left(180)
forward(25)

right(90)
forward(30)







exitonclick()


