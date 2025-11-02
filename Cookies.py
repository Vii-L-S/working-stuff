CookieJar = 10
z=0
def eat(x):
    global CookieJar
    CookieJar = CookieJar - x
def bake(y):
     global CookieJar
     CookieJar = CookieJar + y
def Theif() :
    global CookieJar
    if CookieJar>0:
        x=CookieJar   
        x=x-1
        global z
        z=z+1
        print ('A theif thinks they stole a cookie. They think that you only have', x, 'cookies left.')
        print ('The theif thinks they have stolen', z, 'cookies.')
    else:
        print ('The Theif notices you have no cookies left, they steal £5 instead!!')
while True:
    x=int(input('How many cookies would you like to eat? '))
    y=int(input('How many cookies would you like to bake? '))
    print ('Jar has ', CookieJar)
    eat(x)
    if CookieJar<0:
        CookieJar=0
        print('The jar has ran out. Jar has', CookieJar)
    else:
        print ('You ate', x, 'cookies! Jar has', CookieJar)
    bake(y)
    if CookieJar>20:
        CookieJar=20
        print('Its over capacity. Jar has', CookieJar)
    else:
        print ('You baked', y, 'cookies! Jar has', CookieJar)
    Theif()
        
