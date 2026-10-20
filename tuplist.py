# PASSWORD STRING
password = '19,0,2,7,14,12,4,19,4,17'
 
# STRING OF LETTERS AND INDEX NUMBER
# NUMBER  0 1 2 3 4  ...................................... 25
letters ='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
# WE CAN SPLIT IT INTO A LIST WE CAN LOOP OVER
letters = letters.split(',')
 
 
counter = 0
for L in letters :
    print( counter , ' is Letter' , L )
    counter = counter + 1
 
 
# THE PASSWORD IS A STRING
# WE CAN SPLIT IT INTO A LIST WE CAN LOOP OVER
password = password.split(',')
print( password , 'is type' , type ( password ) )
 
 
# NEW EMPTY STRING FOR CONCATINATION
answer = ''
 
# LOOP OVER EACH NUMBER OF THE PASSWORD
for number in password :
    #print(number)
    number = int( number )  # MAKE AN INTEGER NUMBER
    ltr = letters[ number ] # GET INDEX KEY FROM LETTERS
    print('Number' , number , 'is letter', ltr)
 
    # CONCATINATE (append) EACH LETTER TO THE ANSWER STRING
    answer = answer + ltr
 
 
print('=========================')
print( 'The cracked password is' , answer )
 
 
 
