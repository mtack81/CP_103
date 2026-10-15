speed = 1
screen_width = 600
screen_height = 400

import turtle
import random
import time
import math

# OUR DRAWING SCREEN
turtle.setup( screen_width , screen_height )
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height, startx=10, starty=10)


# MAKE OUR HERO OBJECT
hero = turtle.Turtle()
hero.shape( "turtle" ) # arrow, circle, square, triangle, turtle
hero.shapesize( 1 )
hero.speed( speed )


# MAKE OUR GEM OBJECT
gem = turtle.Turtle()
gem.shape( "triangle" ) # arrow, circle, square, triangle, turtle
gem.shapesize( 2 )
gem.speed( speed )
gem.color('purple')

def vector_motion( ax , ay , tx , ty , steps ):
    
    dx = tx - ax
    dy = ty - ay
    distance = ( dx ** 2 + dy ** 2 ) ** 0.5
    
    if distance == 0:
        dx = 0
        dy = 0
    
    else:
        dx = ( dx / distance ) * steps
        dy = ( dy / distance ) * steps
        
    nx = ax + dx
    ny = ay + dy
    
    return nx , ny , distance
    

# SET RANDOM HERO POSITION !!   MUST BE WHOLE INTEGER NUMBER   int()
x = random.randint( -int( screen_width  / 2 ) , int( screen_width  / 2 ) )
y = random.randint( -int( screen_height / 2 ) , int( screen_height / 2 ) )
hero.penup()
hero.goto( x , y )
hero.pendown()


# SET RANDOM GEM POSITION !!   MUST BE WHOLE INTEGER NUMBER   int()
x = random.randint( -int( screen_width  / 2 ) , int( screen_width  / 2 ) )
y = random.randint( -int( screen_height / 2 ) , int( screen_height / 2 ) )
gem.penup()
gem.goto( x , y )
gem.pendown()


score = 0
mode = 'game'          # SET GAME MODE
while mode == 'game':  # KEEP LOOPING AS LONG AS WE ARE IN GAME MODE

    # GET X and Y COORDINATES OF HERO
    hx = hero.xcor()
    hy = hero.ycor()

    # GET X AND Y COORDINATES OF GEM
    gx = gem.xcor()
    gy = gem.ycor()

    # PASS HERO AND GEM X,Y COORDINATES TO VECTOR MOTION FUNCTION
    # SET RETURNED VALUES FROM VECTOR FUNCTION AS NEW VARIABLES
    new_x , new_y , distance = vector_motion( hx , hy , gx , gy , speed )

    # MOVE TO X,Y POSITION
    hero.goto( new_x , new_y )

    # GIVE SOME FEEDBACK TO THE USER
    print( '\n\n\n' )
    print( 'Coordinates:' , new_x , new_y )
    print( 'Distance to Gem:' , distance )

    # ARE WE CLOSE ENOUGH TO COLLECT THE GEM?
    if distance <= 2:
        score = score + 1 # ADD 1 TO OUR SCORE
        print( 'Got a Gem !!' )
        mode = 'game over'  # EXIT THE GAME LOOP

print( 'Final Score:' , score )
#input( 'End of Game: Press Enter' )
