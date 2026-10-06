
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
# GROWING LINE BOX
move = 10
extend = 10
lines_wanted = 50
counter = 0 # START COUNTING LINES

# IF YOU LOOK AT THE CODE BELOW YOU WILL NOTICE
# WE DRAW 2 LINES FOR EACH ITERATION OF THE LOOP
# SO TO GET AN ACCURATE LINE COUNT WE NEED TO
# DIVIDE THE NUMBER OF LINES WANTED BY 2

for line in range( int( lines_wanted / 2 )):

    hero.forward( move ) #  DRAW A LINE
    hero.right( 90 )

    counter = counter + 1

    hero.forward( move )
    hero.right( 90 )

    counter = counter + 1

    move = move + extend

print( 'Final Line Count' , counter )


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
