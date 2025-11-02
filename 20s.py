import random

answer=random.randrange(1, 20)
x=0
guess=int(input('Pick a number. '))
while (x<7):
    if guess==answer:
        x=7
        print ('Correct!')
    else:
        x=x+1
        if x==6:
            print ('You fail')
            print ('Correct Answer was -')
            print (answer)
        else:
            if guess>answer:
                print ('lower')
            else:
                print ('higher')
            guess=int(input('Pick a new number. '))
