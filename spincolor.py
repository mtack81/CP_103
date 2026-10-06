
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
# SPINNING SHAPES
number_of_sides_on_shape = input('How many sides does your shape have?') or 4
number_of_sides_on_shape = int( number_of_sides_on_shape )

size = 100
counter = 0
rotate_degrees = 15
number_of_shapes = int( 360 / rotate_degrees )
for quantity in range( int( 360 / rotate_degrees )):
    color = 'white' # ALWAYS SET A DEFAULT COLOR

    counter = counter + 1  # UPDATE COUNTER

    if counter == 1: color = 'yellow'
    if counter == 2: color = 'red'
    if counter == 3: color = 'blue'
    if counter == 4: color = 'green'
    if counter == 5: color = 'orange'
    if counter == 6: color = 'purple'

    print( counter , color )
    if counter >= 6: counter = 0  # RESET COUNTER

    hero.color( color )
    hero.right( rotate_degrees )
    for shape in range( number_of_sides_on_shape ):
        hero.forward( size )
        hero.right( 360 / number_of_sides_on_shape )
    hero.penup()
    hero.goto(0,0)
    hero.pendown()

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
