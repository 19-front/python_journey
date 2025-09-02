import random
import turtle
t = turtle.pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green', 'orange',
           'purple', 'white', 'gray']
for n in range(50):
    # generate a random (x,y) location on the screen
    t.pencolor(random.choice(colors)) #pick a random color
    size = random.randint(10,40)  #pick a random spiral size
    # generate a random (x,y) location on the screen
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)