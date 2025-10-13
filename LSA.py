def num():
    x = int(input('Please enter a number: '))
    return x
def list():
    global lis
    lis= (num(), num(), num(), num(), num(), num())
def large():
    global lis
    L = max(lis)
    print (f'The largest number is {L}')
def small():
    global lis
    S = min(lis)
    print (f'The smallest number is {S}')
def average():
    global lis
    A = sum(lis)/len(lis)
    print(f'The average of the list is {A}')
def main():
    list()
    large()
    small()
    average()

if __name__ == '__main__':
    main()
