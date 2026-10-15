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

hash_size = 6
font_size = 20
number_of_ids = 10

def make_random_hash( size ):
    output = ''
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range( size ):
        rc = random.choice( chars )
        output = output + str( rc )
        print( i , 'Building Random Hash: ' , output )
    return output

for i in range( number_of_ids ):

    h = make_random_hash( hash_size )

    random_name = 'ID-' + str( h )

    print( 'Random name:', i , random_name , '\n\n')

    x = -200 + ( font_size * 2 ) * i
    y = -200 + ( font_size * 2 ) * i

    hero.penup()
    hero.goto( x , y )
    hero.pendown()

    style = ( 'Arial' , font_size , 'bold' )

    hero.write( random_name , font=style , align="center" )

turtle.done()

