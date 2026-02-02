"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = [ 20, 40, 30, 70, 30, 55, 75, 15 ]
lefts = [ 10, 20, 30, 40, 50, 60, 70, 80 ]
colors = [  "red", "blue", "green" ]

for  i in range(8):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i % len(colors)]


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

