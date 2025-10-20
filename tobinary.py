x = int(input('Please enter a number: '))
def toBinary(num):
    Blist = []
    while num>0:
        if num%2 == 1:
            Blist.insert(0, '1')
        else:
            Blist.insert(0, '0')
        num = num//2
    bstr = ''.join(Blist)
    return bstr
print(toBinary(x))
