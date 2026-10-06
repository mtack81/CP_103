
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
# ANALOG CLOCK TIMER

for hour_in_day in range( 1 , 25 ):
    print('Time of Day Wanted:', hour_in_day)
    hero.home()
    size = 150
    turn = 360/12 # CALCULATE DEGREES TO TURN
    hero.left( 2 * turn ) # START FACING 1 o'clock POSITION
    for hour in range( 1 , 13 ):

        text = ' ---- '+ str(hour)
        print(text)

        hero.color('black')

        wanted = hour_in_day
        if hour_in_day > 12:
            wanted = hour_in_day - 12

        if hour == wanted:
            hero.color('red')

        hero.pendown()
        hero.stamp()
        hero.forward(size)
        hero.stamp()
        hero.write(text)
        hero.backward(size)
        hero.right(turn)

    time.sleep( 1 )
    #turtle.clearscreen()

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
