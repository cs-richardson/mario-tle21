
    
while True: 
    pyramid_height = int(input("Please Enter How Tall You Want the Pyramid to Be (1-23): "))
    if pyramid_height >= 1 and pyramid_height <= 23: #If pyramid height input is valid then it would break the infinite loop
        break
    else: #If pyramid height input is invalid then it would loop over and over again
        print ("Sorry, Invalid Input") 
        

for i in range (pyramid_height): 
    print (" " * (pyramid_height-1-i), end=" ") #the spaces before the pyramid hashes is the user input subtracted by 1 and it countinues to subtract by 1 each line
    print ("#" * (i+2)) #the amount of hashes is 2 plus with 1 per line after that, e.x 2,3,4,5... 





    

    
