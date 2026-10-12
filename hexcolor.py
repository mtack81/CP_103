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

def make_random_hex_color():
    hex_values = '0123456789ABCDEF'
    hex_color = '#'
    for i in range( 6 ):
        random_choice = random.choice(hex_values)
        random_choice = str( random_choice )
        hex_color = hex_color + random_choice

        print( 'Building Random Hex Color:' , hex_color )
    print( 'Final Hex Color:' , hex_color )
    return hex_color

for i in range( 5 ):
    hex_color = make_random_hex_color()
    hero.color( hex_color )
    time.sleep( 1 )

