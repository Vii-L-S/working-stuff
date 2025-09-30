import random
def flip(heads=0, tails=0):
    global y
    for x in range(y):
        result = random.randint(1, 2)
        if result==1:
            heads +=1
        else:
            tails += 1
    return heads, tails
def main():
    global y
    y = int(input('Please insert the amount of times the coin should be flipped: '))
    heads, tails = flip()
    print(f'Heads: {heads}, Tails: {tails}')

if __name__ == '__main__':
    main()
