import random

while True:
    flip = random.randint(1,2)
    play = int(input('Heads(1) or Tails(2)? '))
    if flip == 1:
        print('It landed on Heads')
    else:
        print('It landed on Tails')
    if flip == play:
        print('You win!!')
    else:
        print('Wrong!! You lose!!')
