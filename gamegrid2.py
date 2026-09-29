# Loop 5 GAME GRID WITH (H)ERO AND (G)EM

hero_x = 2
hero_y = 3

gem_x = 3
gem_y = 1

for y in range( 5 ):
    for x in range( 5 ):
        if x == hero_x and y == hero_y:
            print( 'H' , end = '' )
        elif x == gem_x and y == gem_y:
            print( 'G' , end = '' )
        else:
            print( '_' , end = '' )
    print('') # END OF ROW
print('===================')

