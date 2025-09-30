CookieJar = 10

def eat(x):
    global CookieJar
    CookieJar = CookieJar - x
def bake(x):
     global CookieJar
    CookieJar = CookieJar + x

while True:
    x=input('Are you baking or eating? '))
    if x=='bake':
        x=int(input('How many? ')
        bake(x)
    elif x=='eat':
        x=int(input('How many? ')
        eat(x)
    else print ('only say bake or eat')
    if CookieJar<0:
        print('ITS EMPTY IDIOT')
        CookieJar=CookieJar+1
    elif CookieJar>20:
        print('HOW MANY DO YOU NEED??')
        CookieJar=CookieJar-1
    else:
        print(CookieJar, 'Cookies in jar')
