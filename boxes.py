
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
# BOXES OF COLORS

size = 80
gap = 10
counter = 0
number_of_boxes = 7
hero.pensize( 4 )
hero.goto( int( -canvas_width / 2 ) , 0 ) # MOVE TO LEFT SIDE OF CANVAS

for b in range( number_of_boxes ):

    # ADD COLORS
    color = 'black' # ALWAYS SET A DEFAULT COLOR
    counter = counter + 1  # UPDATE COUNTER
    #---------------------------------------------
    if counter == 1: color = 'red'
    if counter == 2: color = 'green'
    if counter == 3: color = 'blue'
    if counter == 4: color = 'orange'
    if counter == 5: color = 'purple'
    if counter == 6: color = 'yellow'
    #---------------------------------------------
    print( counter , color )
    if counter >= 6: counter = 0  # RESET COUNTER


    hero.color( color ) # CHANGE TURTLE COLOR

    # THIS LOOP WAS YOUR OLD BOX CODE
    for side in range(4):
        hero.forward(size)
        hero.right(90)

    # ADD A GAP BETWEEN BOXES
    hero.forward( size + gap )

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
