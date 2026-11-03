import os
import pygame
import random, time, math
from pygame.locals import *
 
 
#=======================================================================
#               VARIABLES
#=======================================================================
 
 
FPS = 15 # GAME FRAMES PER SECOND
# FULL 1080p RESOLUTION
canvas_width  = 1920
canvas_height = 1080
 
 
#=======================================================================
#               MAKE A CUSTOM OOP OBJECT
#=======================================================================
class myObject:
    timestamp = time.time()
    def __init__(self,dob=timestamp):
        print (f"Unix Timestamp:{dob}")
        self.dob = dob
        
    def rotate_around_object(self,thing):
        self.degrees+= self.speed
        self.degrees = self.degrees % 360
        
        radians = ( self.degrees ) * ( math.pi / 180 )
        self.x = thing.x + ( self.distance * math.cos( radians ) )
        self.y = thing.y + ( self.distance * math.sin( radians ) )
        return self
 
 
 
#=======================================================================
#               CREATE OUR PLANET OBJECTS
#=======================================================================
# NEW EMPTY LIST TO HOLD ALL OUR PLANETS
list_of_planets=[]
 
 
# CREATE SUN OBJECT
sun = myObject()
sun.x = canvas_width / 2
sun.y = canvas_height / 2
sun.radius = 40
sun.color = ( 255 , 255 , 0 )
sun.speed = 0
 
 
earth = myObject()
earth.x = 0 
earth.y = 0
earth.radius = 12
earth.color = ( 0 , 0 , 255)
earth.speed = 4
earth.distance = 120
earth.degrees = 20

list_of_planets.append(earth)

mars = myObject()
mars.x = 0
mars.y = 0
mars.radius = 8
mars.color = (255 , 0 , 0)
mars.speed = 2
mars.distance = 211
mars.degrees = 140

list_of_planets.append(mars)

mercury = myObject()
mercury.x = 0
mercury.y = 0
mercury.radius = 8
mercury.color = (150 , 150 , 150)
mercury.speed = 8
mercury.distance = 62
mercury.degrees = 40

list_of_planets.append(mercury)

venus = myObject()
venus.x = 0
venus.y = 0
venus.radius = 10
venus.color = (225, 200 , 140)
venus.speed = 6
venus.distance = 90
venus.degrees = 90

list_of_planets.append(venus)

jupiter = myObject()
jupiter.x = 0
jupiter.y = 0
jupiter.radius = 25
jupiter.color = (190, 150 , 110)
jupiter.speed = 2
jupiter.distance = 225
jupiter.degrees = 180

list_of_planets.append(jupiter)

saturn = myObject()
saturn.x = 0
saturn.y = 0
saturn.radius = 22
saturn.color = (220, 195 , 140)
saturn.speed = 1.5
saturn.distance = 350
saturn.degrees = 225

list_of_planets.append(saturn)
 
uranus = myObject()
uranus.x = 0
uranus.y = 0
uranus.radius = 15
uranus.color = (150, 210 , 220)
uranus.speed = .8
uranus.distance = 410
uranus.degrees = 275

list_of_planets.append(uranus)

neptune = myObject()
neptune.x = 0
neptune.y = 0
neptune.radius = 17
neptune.color = (50, 90 , 220)
neptune.speed = .8
neptune.distance = 410
neptune.degrees = 275

list_of_planets.append(neptune)

moon = myObject()
moon.x = 0
moon.y = 0
moon.radius = 5
moon.color = (150, 150, 150)
moon.speed = 12
moon.distance = 20
moon.degrees = 0

ship = myObject()
ship.x = 1800
ship.y = 540
ship.speed = 3
 
# ======================================================================
#
# ======================================================================
os.environ['SDL_VIDEO_CENTERED'] = '1' # COMMENT THIS LINE IF IT GIVES YOU AN ERROR
pygame.init()   # YOU HAVE TO CALL THIS AT THE START
canvas = pygame.display.set_mode((canvas_width, canvas_height))
clock  = pygame.time.Clock()
 
 
mode = 'game'
loopcount = 0
while mode == 'game':
 
    loopcount += 1
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
                pygame.quit()
                exit()
 
 
    # =============================
    # DRAW EVERYTHING TO THE CANVAS
    # =============================
 
    # GAME BACKGROUND COLOR
    white = (255 , 255 , 255)   # RGB COLOR TUPLE FOR WHITE
    black = (  0 ,   0 ,   0)   # RGB COLOR TUPLE FOR BLACK
    canvas.fill( black )
 
    # DRAW SUN TO CANVAS
    pygame.draw.circle(canvas, sun.color, ( sun.x , sun.y ), sun.radius)
 
 
    for planet in list_of_planets:
        planet.rotate_around_object(sun)
        pygame.draw.circle (canvas, planet.color, ( planet.x , planet.y ), planet.radius)
        
    moon.rotate_around_object(earth)
    pygame.draw.circle(canvas, moon.color, (moon.x, moon.y), moon.radius)
    
    ship.x -= ship.speed

        
    pygame.draw.ellipse(canvas, (100, 100, 100),
                        (ship.x, ship.y, 80, 30))

    
    pygame.draw.polygon(canvas, (70, 70, 70),
                        [(ship.x + 10, ship.y + 15),
                         (ship.x - 20, ship.y),
                         (ship.x + 5, ship.y + 30)])

    
    pygame.draw.polygon(canvas, (70, 70, 70),
                        [(ship.x + 65, ship.y + 15),
                         (ship.x + 100, ship.y),
                         (ship.x + 75, ship.y + 30)])

    
    pygame.draw.ellipse(canvas, (180, 180, 180),
                        (ship.x + 30, ship.y + 5, 20, 20))
    # LOOP OVER EACH PLANET IN THE LIST OF PLANETS AND CALL THE OOP METHOD / FUNCTION
 
 
    # CALL THE OOP METHOD / FUNCTION FOR MOON ROTATING AROUND EARTH
    # CALL THE OOP METHOD / FUNCTION FOR MOON ROTATING AROUND EARTH
    # CALL THE OOP METHOD / FUNCTION FOR MOON ROTATING AROUND EARTH
    # CALL THE OOP METHOD / FUNCTION FOR MOON ROTATING AROUND EARTH
 
 
    # UPDATE EVERYTHING ON CANVAS !!
    pygame.display.update()
 
    # GAME SPEED IN FRAMES PER SECOND
    clock.tick(FPS)
