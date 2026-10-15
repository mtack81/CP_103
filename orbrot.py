speed = 1
screen_width = 400
screen_height = 400

import turtle
import random
import time
import math

def rotate_around_object( sun_x , sun_y , planet_distance , planet_degrees ):
    # MATH TO CALCULATE ROTATION AROUND A POINT
    radians = ( planet_degrees ) * ( math.pi / 180 ) # ANGLE MUST BE IN RADIANS
    planet_x = sun_x + ( planet_distance * math.cos( radians )) # CALCULATE NEW X COORDINATE
    planet_y = sun_y + ( planet_distance * math.sin( radians )) # CALCULATE NEW Y COORDINATE
    return planet_x , planet_y # RETURN NEW X,Y COORDINATES

# OUR DRAWING SCREEN
turtle.setup( screen_width , screen_height )
screen = turtle.Screen()
screen.bgcolor( 'black' )


# SUN OBJECT
sun = turtle.Turtle()
sun.shape( "circle" ) # arrow, circle, square, triangle, turtle
sun.shapesize( 4 )
sun.speed( speed )
sun.color( 'yellow' )
# OBJECT POSITION
sun_x = 0
sun_y = 0



# PLANET OBJECT
planet = turtle.Turtle()
planet.shape( "circle" ) # arrow, circle, square, triangle, turtle
planet.shapesize( 2 )
planet.speed( speed )
planet.color('blue')
# OBJECT POSITION
planet_x = 100
planet_y = 0
planet_distance = 100
planet_degrees = 0



planet.penup()
planet.goto( planet_x , planet_y )


orbits = 0             # ORBIT COUNTER
mode = 'game'          # SET GAME MODE
while mode == 'game':  # KEEP LOOPING AS LONG AS WE ARE IN GAME MODE

    # GET X AND Y COORDINATES OF PLANET
    planet_x = planet.xcor()
    planet_y = planet.ycor()

    # CALL OUR FUNCTION AND GET RETURNED CALCULATIONS
    new_x , new_y = rotate_around_object( sun_x , sun_y , planet_distance , planet_degrees )

    planet.goto( new_x , new_y )           # GO TO NEW POSITION
    planet_degrees = planet_degrees + 1    # ROTATE 1 DEGREE

    if planet_degrees >= 360:              # DID WE COMPLETE A CIRCLE ?
        planet_degrees = 0                 # RESET OUR DEGREES BACK TO ZERO
        orbits = orbits + 1                # INCREMENT OUR ORBIT COUNTER

    # GIVE SOME FEEDBACK TO THE USER
    print( '\n\n\n' ) # ADD SOME BLANK LINES FOR SPACING
    print( 'Coordinates:' , int( new_x ) , int( new_y ) )
    print( 'Number of Years:' , orbits )


