# Loop 1 - A 5x3 GAME GRID
for y in range( 3 ):
    for x in range( 5 ):
        print( '_' , end = ',' )
    print('') # END OF ROW
print('===================')



# Loop 2 - 5x5 GAME GRID WITH A (H)ERO

# DEFINE THE HERO POSITION
hero_x = 2 # X COORDINATE
hero_y = 3 # Y COORDINATE

for y in range( 5 ):
    for x in range( 5 ):
        if x == hero_x and y == hero_y:
            print( 'H' , end = '' )
        else:
            print( '_' , end = '' )
    print('') # END OF ROW
print('===================')


