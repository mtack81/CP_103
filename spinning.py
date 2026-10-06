
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

size = 100
rotate_hero = 90
rotate_shape = 15

number_of_sides_on_shape = 4
number_of_sides_on_shape = input('How many sides does your shape have?') or 4
number_of_sides_on_shape = int( number_of_sides_on_shape )
rotate_hero  = int( 360 / number_of_sides_on_shape )

number_of_shapes_wanted = 3
number_of_shapes_wanted = input('How many shapes do you want?') or 3
number_of_shapes_wanted = int( number_of_shapes_wanted )
rotate_shape = int( 360 / number_of_shapes_wanted )

for quantity in range( number_of_shapes_wanted ):
    hero.right( rotate_shape )

    for shape in range( number_of_sides_on_shape ):

        hero.forward( size )

        hero.right( rotate_hero )

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
