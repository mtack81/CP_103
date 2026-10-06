
#=======================================================================
#--->--->--->--->--->--->   CONFIGURATION VARIABLES
#=======================================================================

default_speed = 9
canvas_width  = 600
canvas_height = 400

#=======================================================================
#--->--->--->--->--->--->   IMPORT MODULES AND START DRAWING
#=======================================================================
import turtle
import time

# OUR DRAWING CANVAS
# OUR DRAWING CANVAS
screen = turtle.Screen()
screen.setup(width=canvas_width, height=canvas_height, startx=10, starty=10)




# MAKE OUR HERO OBJECT
hero = turtle.Turtle()
hero.shape( "circle" )
hero.color( "black" )
hero.shapesize( 1 )
hero.speed( default_speed )


#=======================================================================
#--->--->--->--->--->--->   WRITE YOUR CODE BELOW
#=======================================================================
# ANALOG CLOCK
size = 150
turn = 360/12 # CALCULATE DEGREES TO TURN

# TURTLE STARTS FACING THE 3 o'clock HAND.
# SO WE NEED TO TURN HERO LEFT 2 times the turn angle.
# THIS WAY HERO STARTS AT THE 1 o'clock HAND.

hero.left( 2 *  turn ) # CALCULATE 2 * THE TURN ANGLE


# LOOP OVER HANDS OF THE CLOCK
# MUST BE 1,2,3,4,5,6,7,8,9,10,11,12 IN THAT ORDER

for hour in range( 1 , 13 ):
    text = ' ---- '+ str(hour) + " - O'Clock"
    print(text)
    hero.forward(size)
    hero.stamp()
    hero.write(text)
    hero.backward(size)
    hero.right(turn)

#=======================================================================
#--->--->--->--->--->--->   END OF CODE AREA
#=======================================================================

# PAUSE AND THEN CLEAR THE SCREEN
time.sleep(1)
#turtle.clearscreen()


print('\n\n\n')
print('Done!')
text='Click the Canvas to Close.'
hero.penup()
hero.goto(-canvas_width/3,0)
hero.write(text, font=("Arial",24,"normal"))
print(text)
# CLICK ON THE CANVAS TO EXIT
screen.exitonclick()
#screen.mainloop()
