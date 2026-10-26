# DO NOT ALTER OR REMOVE
# Collecting Gems Game by Bowhuis
# Version 2026 - 04 - 29 - a - 22:58:32

print(
'''
========================================================================
Your Name
Course and Section #
Date
========================================================================
''')

# IMPORT SOME MODULES
import os
import random
import string


# DEFINE OUR DEFAULT VARIABLES
hero_icon   = 'H'
board_icon  = '_'
gem_icon    = '*'

board_width = 20
board_height = 10
number_of_gems = 8


#=====================================================================================================
#               FUNCTION POOL
#=====================================================================================================


# CLEAR THE OLD TERMINAL SCREEN
def clear():
    print('Clearing Screen')
    # COMMENT THIS CODE IF IT FAILS ON YOUR SYSTEM
    os.system('cls' if os.name == 'nt' else 'clear')


# MAKE A GAME GRID
def make_game_grid( width=9, height=3, icon='-' ):
    grid=[]                     # NEW EMPTY LIST
    for y in range(height):     # LOOP 1
        tmp=[]                  # MAKE A NEW TEMPORARY EMPTY LIST
        for x in range(width):  # LOOP 2 (a nested loop)
            tmp.append(icon)    # ADD ICON TO THE TEMPORARY LIST
        #print(tmp)              # FOR DEBUGGING
        grid.append(tmp)        # ADD TEMPORARY LIST TO MAIN LIST
    #print(grid)                # FOR DEBUGGING
    return grid                 # RETURN THE ANSWER BACK TO THE GAME


# DRAW GRID TO SCREEN
def draw_grid( grid ):
    for y in grid:             # HEIGHT / Y AXIS
        for x in y:            # WIDTH  / X AXIS  (nested loop)
            print(x,end='')
        print('')


#=====================================================================================================
#               END FUNCTION POOL
#=====================================================================================================


# CALL OUR FUNCTION TO CREATE OUR GAME BOARD GRID
grid = make_game_grid( board_width , board_height , board_icon )


# DO SOME MATH TO CALCULATE THE CENTER OF THE SCREEN
center = int( board_width / 2  )     # CALCULATE CENTER X COORDINATE
bottom = int( board_height - 1 )     # WE NEED TO - 1 TO COUNT LIKE A PC !!

# MAKE OUR HERO USING A DICTIONARY
# POSITION HERO AT BOTTOM CENTER OF GAME GRID
hero = {
    "name":'hero' ,
    "x": center,
    "y": bottom,
    "score": 0,
    "health": 10,
    "number_of_moves" : 0
}




# A NEW EMPTY LIST TO STORE ALL GEMS
list_of_gems = []


# GEM 1
# WE NEED TO SUBTRACT 1 TO COUNT LIKE A PC !!
x = random.randint( 0 , board_width - 1 )   # RANDOM X
y = random.randint( 0 , board_height - 1 )  # RANDOM Y
gem = { 'x':x , 'y':y }       # DICTIONARY TO STORE GEMS X,Y COORDINATES
list_of_gems.append( gem )    # APPEND THE GEM TO OUR LIST OF GEMS
grid[ gem['y'] ] [ gem['x'] ] = gem_icon  # DRAW THE GEM TO BOARD


# GEM 2
# WE NEED TO SUBTRACT 1 TO COUNT LIKE A PC !!
x = random.randint( 0 , board_width - 1 )   # RANDOM X
y = random.randint( 0 , board_height - 1 )  # RANDOM Y
gem = { 'x':x , 'y':y }       # DICTIONARY TO STORE GEMS X,Y COORDINATES
list_of_gems.append( gem )    # APPEND THE GEM TO OUR LIST OF GEMS
grid[ gem['y'] ] [ gem['x'] ] = gem_icon  # DRAW THE GEM TO BOARD


for i in range( number_of_gems ):
    x = random.randint( 0 , board_width - 1 )
    y = random.randint( 0 , board_height - 1 )
    gem = { 'x' :x , 'y':y }
    list_of_gems.append( gem )
    grid[ gem['y'] ] [ gem['x'] ] = gem_icon




# PUT HERO ON THE BOARD LAST IN CASE HE IS ON TOP OF A GEM
grid[ hero['y'] ][ hero['x'] ] = hero_icon


# DRAW OUR GAME BOARD
draw_grid(grid)


mode = 'game'
while mode == 'game':  # START THE GAME LOOP

    # !! STORE CURRENT POSITION IN THE DICTIONARY !!
    # WE WILL USE THIS LATER IN OUR CODE
    hero['oldx'] = hero['x']
    hero['oldy'] = hero['y']


    number_of_gems = len( list_of_gems ) # COUNT NUMBER OF GEMS

    # GIVE USER FEEDBACK
    print( 'Moves:' , hero['number_of_moves'] )
    print( 'Hero Score:' , hero['score'] )
    print( 'Gems Remaining: ' , number_of_gems )
    #print( 'Hero Info: ' , hero )
    #print( 'Gem Locations: ',list_of_gems )
    print('\n\n')  # SOME LINE BREAKS

    key = input( ' w, s, a, d, or q  ?  ' )   # PROMPT FOR USER INPUT

    # CALL OUR FUNCTION TO CLEAR OUR OLD TERMINAL OUTPUT
    # COMMENT THE LINE IF IT DOES NOT WORK ON YOUR OS
    clear()


    #===================================================================
    # KEY PRESS EVENTS HERE
    #===================================================================

    if key == 'q':  # ELSE IF
        mode = 'end'
        print( 'Good Bye!' )
        break # BREAK OUT OF THE GAME LOOP



    if key == 'w':
        print( 'Move up.' )
        hero['y'] = hero['y'] - 1
        hero['number_of_moves'] += 1
        
    elif key == 's':
        print( 'Move down.' )
        hero['y'] = hero['y'] + 1
        hero[ 'number_of_moves'] += 1
        
    elif key == 'a':
        print( 'Move left.' )
        hero['x'] = hero['x'] - 1
        hero[ 'number_of_moves'] += 1
        
    elif key == 'd':
        print( 'Move right.' )
        hero['x'] = hero['x'] + 1
        hero[ 'number_of_moves'] += 1
        
    else:
        print( key , 'is invalid.' )

    if hero['x'] <= 0:
        hero['x'] = 0
        
    if hero['x'] >= board_width - 1 :
        hero['x'] = board_width - 1
        
    if hero['y'] <= 0:
        hero['y'] = 0
        
    if hero['y'] >= board_height - 1 :
        hero['y'] = board_height - 1





    #===================================================================
    # MAKE A TEMPORARY LIST
    # USE THIS TO ORGANIZE DATA THAT WE WANT TO KEEP, DISCARD, ETC.
    tmp = []

    # LOOP OVER ALL THE GEMS
    # TEST IF WE WANT TO KEEP OR IGNORE EACH GEM
    for gem in list_of_gems:

        do = 'show_gem' # DEFAULT TO KEEP THE GEM ON THE BOARD

        if gem['x'] == hero['x'] and gem['y'] == hero['y']:
            do = 'collect'
            
            hero['score'] = hero['score'] + 1




        # ADD THE GEM TO THE TMP LIST IF WE DID NOT COLLECT IT
        if do == 'show_gem':
            tmp.append( gem )
            grid[ gem['y'] ] [ gem['x'] ] = gem_icon  # DRAW THE GEM TO BOARD


    # UPDATE THE LIST OF GEMS WITH WHAT WE SAVED IN TMP
    list_of_gems = tmp[:]

    # WE DON'T NEED TMP ANY MORE. DELETE IT.
    del tmp


    #===================================================================
    # UPDATE OUR HERO ICON

    grid[ hero['oldy'] ] [ hero['oldx'] ] = board_icon # SWAP OLD HERO ICON WITH THE BOARD ICON

    grid[ hero['y'] ] [ hero['x'] ] = hero_icon # SWAP OLD BOARD ICON WITH THE HERO ICON


    # DRAW GRID TO SCREEN
    draw_grid( grid )



print(hero)


