import  turtle

# Create a graphic window
graphicWindow = turtle.Screen()

# Create a turtle and named it alexTurtle
# alexTurtle is pointing to an instance of the Class turtle which is located in turtle package/module
alexaTurtle = turtle.Turtle()

# Tell alexaTurtle to move forward by 200 units
alexaTurtle.forward(200)

# Tell alexaTurtle to turn left by 90 degree
alexaTurtle.left(90)

# Complete the second side of rectangle
alexaTurtle.forward(200)

# Completing the rectangle
alexaTurtle.left(90)
alexaTurtle.forward(200)
alexaTurtle.left(90)
alexaTurtle.forward(200)
graphicWindow.exitonclick()

# Creating instance variable salary
alexaTurtle.salary = 5000

# Printing the salary
print("Salary of Alexa is : ",alexaTurtle.salary)
