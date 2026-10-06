
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
turtle.bgcolor("black")

hero.pensize(2)

spiral_size = 4
spiral_grow = 1
spiral_angle = 50
number_of_spirals = 150
hero.speed( 9 )
counter = 0
for i in range(number_of_spirals):


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



    hero.shapesize( 0.4 )
    hero.forward(spiral_size)
    hero.right(spiral_angle)
    spiral_size = spiral_size + spiral_grow
    hero.shapesize( 0.25 )
    hero.stamp()

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
