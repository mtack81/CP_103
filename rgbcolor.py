import turtle
import time

# OUR DRAWING CANVAS
turtle.setup( 600 , 400 )
screen = turtle.Screen()
screen.setup(width=600, height=400, startx=10, starty=10)



# MAKE OUR HERO OBJECT
hero = turtle.Turtle()
hero.shape( "turtle" ) # arrow, turtle, circle, square triangle
hero.shapesize( 8 )
hero.speed( 9 )

import random
turtle.colormode( 255 )

def make_random_rgb_color():
    red = random.randint( 0 , 255 )
    green = random.randint( 0 , 255 )
    blue = random.randint( 0 , 255 )
    rgb = ( red , green , blue )
    print( 'Random Red, Green, Blue:' , rgb )
    return rgb

for i in range( 5 ):
    rgb = make_random_rgb_color()
    hero.color( rgb )
    time.sleep( 1 )

