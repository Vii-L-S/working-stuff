def age():
    global old
    old = int(input('How old are you? '))

x = 1

while x ==1:
    age()
    if old>130 or old<0:
        print ('Your age is wrong, try again')
    elif old<=130 and old>=0:
        print ('Your age is correct')
        x=0
