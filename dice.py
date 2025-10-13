import random

d1 = random.randrange(1, 7)
d2 = random.randrange(1, 7)
tries = 1
while d1 != d2:
    tries = tries + 1
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
else:
    if tries > 1:
        print(f'It took {tries} tries to roll a double')
    else:
        print(f'It took {tries} try to roll a double')
