power = 100
high = 60
medium = 30
low = 10

for minutes in range(5,120,5):
    power = power * 0.9 # LOSS OF POWER EVERY 5 MINUTES
    print( 'Run Time' , minutes , 'Minutes. Power Level' , end=' ')
    if power >= high:
        print( 'High' , power )
    elif power >= medium:
        print( 'Medium' , power )
    elif power >= low:
        print( 'Low' , power )
    elif power < low:
        print( 'DANGER' , power )
