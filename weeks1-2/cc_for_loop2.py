# for loop in range function
for x in range(0,6,1):
        if x == 0 or x == 6 :          #check if 0,6 equals x
                print('*')             #print *
        elif x == 1 or x == 5 :        #check if 1,5 equals x
                print('**')            #print **
        elif x == 2 or x == 3 :        #check if 2,3 equals x
                print('***')           #print ***
        else :
                print('****')          #print ****