
name = input ('Enter a name') or 'Bob'
print( 'You entered the name' , name)
print( type ( name) )

number = input ('Enter a number') or '4'
print( 'You entered the number' , number)
print( 'Original Type is a ' , type ( number ) )
print( 'Forced to be an integer number' , type ( int( number)))
print( 'Forced to be a float decimal' , type (float(number)))
