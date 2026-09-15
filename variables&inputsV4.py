# Variable      User Input        or      Default
 
v1 = input('Enter your favorite type of dog. ') or 'Boston Terrier'
v2 = input('Enter an obvious feature ') or 'Ears'
v3 = input('Enter how many colors of the dog that there are ') or '4'
v4 = input('Enter how many legs they have ') or '4'
v5 = input('Enter how active the dog is ') or 'lazy'
v6 = input('Enter how you feel about them ') or 'love'
 
 
print('================================')
 
print( v1 , ' | The ', v1 , ' is my favorite type of dog.')
print( v2 , ' | People always notice their ' , v2 , '.')
print( v3 , ' | There\'s exactly' , v3 , 'colors and they have large ', v2 ,' on the ' , v1 , '.')
print( v4 , ' | They have' , v4 , ' legs and love not using them at all.')
print( v5 , ' | In addition to large' , v2 ,  'and being ' , v5 , 'they smell pretty bad.' )
print( v6 , ' | Overall ' , v1 , ' is the perfect dog to' , v6 , '.')
