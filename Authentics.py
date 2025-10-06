x = False
att = 0
while x==False and att<5:
    user = input('Enter username: ')
    pssw = input('Enter password: ')
    if user=='admin' and pssw=='passwd':
        print('Access Allowed')
        x = True
    else:
        print('Access denied')
        att= att+1
