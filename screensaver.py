# DO NOT ALTER OR REMOVE
# OOP and UML Design
# Version 2026 - 03 - 20 - a - 04:36:01
 
print(
'''
========================================================================
Your Name
Course and Section #
Date
OOP INTRO: CODE A SCREENSAVER
========================================================================
 
!! SEE LECTURE NOTES !!
DRAW A UML CLASS DIAGRAM FOR A HERO WITH THE FOLLOWING ATTRIBUTES HERE
name, x_coordinate, y_coordinate, color
 
UML Diagram of the Rectangle Class
|-----------------------------|
|      Rectangle              |
|-----------------------------|
| + name  : string            |
| + xcord : integer           |
| + ycord : integer           |
| + color  : string           |
|-----------------------------|
| + __init__(self,n,x,y,c)    |
| + __str__():string          |
| + drawit()                  |
|-----------------------------|
 
 
UML Instances
|-----------------|    |-------------------|
| box1:rectangle  |    | box2:rectangle    |
|-----------------|    |-------------------|
| name  = 'hero1' |    | name = 'hero2'    |
| xcord = 10      |    | xcord = 60        |
| ycord = 10      |    | ycord = 20        |
| color = 'green' |    | color = 'red'     |
|-----------------|    |-------------------|
''')
 
 
#=======================================================================
#               IMPORT MODULES
#=======================================================================
 
import os
import pygame
import random, time, math
from pygame.locals import *
 
#=======================================================================
#               VARIABLES
#=======================================================================
 
FPS   = 15   # FRAMES PER SECOND OF VIDEO
delay = 1    # SECONDS TO DELAY GAME UPDATE
timer = 0    # TO KEEP TRACK OF DELAYED TIME
 
 
#=======================================================================
# MAKE A LIST OF SHAPES HERE
#=======================================================================
 
# LIST OF POSSIBLE SHAPES AND NUMBER RANGE OF EACH SHAPE TO MAKE
min_number_of_shapes = 2
max_number_of_shapes = 6
list_of_possible_shapes = [ 'box' , 'circle' , 'line' , 'triangle' , 'polygon' ]
 
 
# FULL 720p RESOLUTION
canvas_width  = 1080
canvas_height = 720
 
# FOR TESTING
canvas_width  = 640
canvas_height = 400
 
 
# COMMON RGB COLOR TUPLES
white  = (255 , 255 , 255)
black  = (  0 ,   0 ,   0)
red    = (255 ,   0 ,   0)
green  = (  0 , 255 ,   0)
blue   = (  0 ,   0 , 255)
 
 
#=======================================================================
#               MAKE A CUSTOM OOP OBJECT CLASS
#=======================================================================
class myObject: # CREATE AND NAME A CLASS
    def __init__( self , t ): # INSTANTIATE (MAKE) A NEW OBJECT
        self.t = str(t)   # (T)YPE OF SHAPE
        self.x = 10
        self.y = 10
        self.w = 100
        self.h = 100
        self.b = 10
        self.c = blue
 
    #=======================================================================
    #               MAKE METHODS aka OOP FUNCTIONS HERE
    #=======================================================================
    def make_random_rgb_color( self ):
        r = random . randrange ( 0 , 255 )
        g = random . randrange ( 0 , 255 )
        b = random . randrange ( 0 , 255 )
        rgb = ( r , g , b )
        self.c = rgb
 
    def randomize( self ):
        self.x = random.randint( 0 , canvas_width )
        self.y = random.randint( 0 , canvas_height )
        self.w = random.randint ( 10 , 400 )
        self.h = random.randint( 10 , 400 )
        self.b = random.randint( 0 , int(obj.w/4) )
        
 
# ======================================================================
#           LOAD PYGAME
# ======================================================================
#os.environ['SDL_VIDEO_CENTERED'] = '1' # COMMENT THIS LINE IF IT GIVES YOU AN ERROR
os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"  # COMMENT THIS LINE IF IT GIVES YOU AN ERROR
pygame.init()   # YOU HAVE TO CALL THIS AT THE START
canvas = pygame.display.set_mode(( canvas_width , canvas_height ))
clock  = pygame.time.Clock()
 
#=======================================================================
#               CREATE OOP OBJECTS AND ADD TO A LIST WE CAN LOOP OVER
#=======================================================================
 
 
list_of_objects = [] # NEW EMPTY LIST
 
obj = myObject( 'box' ) # CREATE AN OBJECT OF TYPE BOX
 
list_of_objects.append( obj ) # ADD BOX OBJECT TO THE LIST OF OBJECTS
 
 
# ======================================================================
#       LOOP AND MAKE MANY SHAPES HERE
# ======================================================================
for shape in list_of_possible_shapes:
    
    random_number = random . randrange ( min_number_of_shapes , max_number_of_shapes )
    
    print( 'Making' , random_number , shape )
    
    for i in range( random_number ):
        
        obj = myObject( shape )
        
        list_of_objects.append( obj )
        
 
 
# ======================================================================
#           START GAME LOOP
# ======================================================================
mode = 'game'
loopcount = 0
while mode == 'game':   # START GAME LOOP
 
    # GAME SPEED
    clock.tick(FPS)
 
    loopcount += 1  # ADD ONE TO OUR COUNTER
    if loopcount > 1000: break # SAFETY CUTOFF
 
    #===================================================================
    # KEY PRESS EVENTS
    #===================================================================
    # SINGLE KEY PRESS
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # PRESS "q" KEY TO QUIT THE GAME
            if event.key == K_q:
                print ("Have a good day.")
                mode='end'
                break # BREAK THE GAME LOOP BUT KEEP RUNNING OTHER CODE AFTER
                pygame.quit() # THIS WOULD EXIT PYGAME
                exit()        # THIS WOULD EXIT PYTHON
 
 
    # =========================================
    # HACK TO DELAY GAME SPEED BY CUSTOM AMOUNT
    # =========================================
    timer += 1 # ADD TO OUR TIMER
    if timer <= FPS * delay: continue
    timer = 0 # RESET TIMER
 
 
    # ==============================
    # UPDATE/MODIFY ALL GAME OBJECTS
    # ==============================
 
    # GAME BACKGROUND COLOR
    canvas.fill( white )
 
 
    # FOR DEBUGGING
    #print('\n\n\n')
    #print( len( list_of_objects ))
    #print( list_of_objects )
 
    #===================================================================
    #       SHUFFLE THE LIST OF SHAPES HERE
    #===================================================================

    random.shuffle( list_of_objects )
 
 
    for obj in list_of_objects: # LOOP OVER OUR LIST OF OBJECTS
 
        # UPDATE THE BOX ATTRIBUTES
        #===================================================================
        #       GET RANDOM SIZES AND COORDINATES FROM "METHOD" "OOP FUNCTION"
        #       GET RANDOM RGB COLOR FROM "METHOD" "OOP FUNCTION"
        #===================================================================
        obj.randomize()
        obj.make_random_rgb_color()
 
 
        #===================================================================
        #       BOXES HERE
        #===================================================================
        if obj.t == 'box':
 
            #      DRAW                COLOR         X       Y     WIDTH     HEIGHT    BORDER LINE
            pygame.draw.rect( canvas , obj.c , ( obj.x , obj.y ,   obj.w  ,  obj.h )  , obj.b )
 
 
 
        #===================================================================
        #       CIRCLES HERE
        #===================================================================
        if obj.t == 'circle':
            
            obj.r = int( obj.w / 2 )
            
            pygame.draw.circle( canvas , obj.c , [obj.x , obj.y] , obj.r , obj.b )
            
 
 
        #===================================================================
        #       LINES HERE
        #===================================================================
 
        if obj.t == 'line':
            
            start_point = ( obj.x , obj.y )
            
            x = random.randint( 0 , canvas_width )
            y = random.randint( 0 , canvas_height )
            end_point = ( x , y )
            
            pygame.draw.line( canvas , obj.c , start_point , end_point , obj.b )
            
 
        #===================================================================
        #       POLYGONS HERE
        #===================================================================
        if obj.t == 'polygon':
            list_of_data_points = []
            start_point = ( obj.x , obj.y )
            list_of_data_points.append( start_point )
            
            n = random.randint( 3 , 6 )
            
            for i in range( n ):
                x = random.randint( 0 , canvas_width )
                y = random.randint( 0 , canvas_height )
                point = ( x , y )
                
                list_of_data_points.append( point )
                
            obj.b = random.randint( 1 , 4 )
            
            pygame.draw.polygon( canvas , obj.c , list_of_data_points , obj.b )
            
 
 
        #===================================================================
        #       TRIANGLES HERE
        #===================================================================
        if obj.t == 'triangle':
            list_of_data_points = []
            
            point = ( obj.x , obj.y )
            list_of_data_points.append( point )
            
            rx = random.randint( -200 , 200 )
            ry = random.randint( -200 , 200 )
            
            point = ( obj.x + rx , obj.y )
            list_of_data_points.append( point )
            
            point = ( obj.x + rx , obj.y + ry )
            list_of_data_points.append( point )
            
            point = ( obj.x , obj.y )
            list_of_data_points.append( point )
            
            obj.b = random.randint( 1 , 2 )
            
            pygame.draw.polygon( canvas , obj.c , list_of_data_points , obj.b )
            
            
 
 
    #===================================================================
    #       DRAW EVERYTHING ON THE CANVAS !!
    #===================================================================
    pygame.display.update()
 
 
print('END OF GAME LOOP')
'''
#========================================================================
# TRUE OOP STYLE
# BROHUIS DOESN'T LIKE THIS SO BROHUIS DOESN'T DO THIS
# BUT YOU SHOULD PROBABLY KNOW IT EXISTS AND IS USED OFTEN IN THE WILD
def myGame():
    sun = myObject()
    print(sun.dob)
    myGame()
 
if __name__ == "__main__":
    myGame()
#========================================================================
'''
 
 
