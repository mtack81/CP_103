# INITIAL DICTIONARY
shopping_cart = { 'milk': 2 , 'eggs' : 4 , 'cheese' : 3 }
 
# EASY WAY TO ADD ITEMS
shopping_cart['bread'] = 3
 
shopping_cart['butter'] = 1
shopping_cart['ham'] = 6
shopping_cart['coffee'] = 14
 
 
 
print(type(shopping_cart))
 
counter = 0
 
for item,price in shopping_cart.items():  # LOOP OVER THE ITEMS
 
    print( item , 'costs $' , price )
    counter = counter + 1
 
print( 'Total number of items = ' , counter )
 
