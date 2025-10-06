OddCount = 0
EvenCount = 0
def ngen():
    import random
    y = random.randrange(0, 100)
    return y


nums = (ngen(), ngen(), ngen(), ngen(), ngen(), ngen())
print (f'Your numbers are {nums}')
for x in(nums):
    if(x%2==0):
        EvenCount = EvenCount+1
    else:
        OddCount = OddCount+1
print(f'Even numbers: {EvenCount}')
print(f'Odd numbers: {OddCount}')
