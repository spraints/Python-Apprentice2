# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'


import turtle

def set_turtle_image(tt, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = tt.getscreen()
    screen.addshape(image_path)
    tt.shape(image_path)

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
set_background_image(screen, "emoji.png")

t = turtle.Turtle()
set_turtle_image(t, "moustache3.gif")
t.speed(1)
t.right(90)
t.forward(50)
t.right(90)
for i in range(10):
    t.forward(20)
    t.backward(20)

def moveit(x, y):
    t.goto(x,y)

screen.onclick(moveit)
turtle.done()