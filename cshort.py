counter = 0
 
for n in range(50):
 
    color = 'black'        # ALWAYS SET A DEFAULT COLOR
    counter = counter + 1  # UPDATE COUNTER
    #---------------------------------------------
    if counter == 1: color = 'red'
    if counter == 2: color = 'green'
    if counter == 3: color = 'blue'
    if counter == 4: color = 'orange'
    if counter == 5: color = 'yellow'
    if counter == 6: color = 'purple'
    #---------------------------------------------
    print( counter , color )
    if counter >= 6: counter = 0  # RESET COUNTER
