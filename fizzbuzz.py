for x in range(1, 101):
    u = input('Count to 100: ') #gets the user response

    if x%3==0 and x%5==0:
        if u != 'fizzbuzz':
            print('Wrong, it was fizzbuzz') # checks if the user response is wrong if the correct answer is fizzbuzz
    elif x%3==0:
        if u != 'fizz':
            print('Wrong, it was fizz') # checks if the user response is wrong when the answer is fizz
    elif x%5==0:
        if u != 'buzz':
            print('Wrong, it was buzz') # checks if the user response is wrong when the answer is buzz
    else:
        if int(u)!=x:
            print(f'Wrong, it was {x}')
