""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()


def set_turtle_image(tt, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = tt.getscreen()
    screen.addshape(image_path)
    tt.shape(image_path)

set_turtle_image(t, "leaguebot_bolt.gif")
t.turtlesize(.005,.005,12)
print(t.turtlesize())
print(t.resizemode())
#t.resizemode("user")

t.penup()
t.speed(3)

for i in range(4):
    t.goto(200, 200)
    t.goto(-200, -200)


turtle.exitonclick()   