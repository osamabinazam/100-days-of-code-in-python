import turtle
graphicWindow =  turtle.Screen()
graphicWindow.bgcolor("blue")

faizan = turtle.Turtle()
faizan.pensize(5)

shafique = turtle.Turtle()
shafique.pensize(10)
shafique.color("hotpink")

# Movement of first turtle
faizan.forward(80)
faizan.left(120)
faizan.forward(80)
faizan.left(120)
faizan.forward(80)
faizan.left(120)
faizan.right(180)
faizan.forward(80)

# Movement of second turtle
shafique.forward(50)
shafique.left(90)
shafique.forward(50)
shafique.left(90)
shafique.forward(50)
shafique.left(90)
shafique.forward(50)
shafique.left(90)

# When someone click on turtle screen then screen will be closed
graphicWindow.exitonclick()
