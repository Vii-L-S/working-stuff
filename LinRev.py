def BLin():
    nlist = [1, 14, 12, 47, 20, 65, 39, 10, 73, 99] # list of items
    found = False
    search = int(input('Enter an integer: '))   # asks user what to search for
    for y in range(len(nlist)):     # loops through the whole list
        if search == nlist[y]:
            found = True    # lets the program know that thew term is found
            pos=y+1    # gets the position of the item in the list
    if found==True:         
        print(f'Found at position {pos}.')
    else:       # if not found, then found is still set to false
        print('Not found.')
def ALin():
    import random   #imports the random library
    nlist = [random.randrange(1, 100) for x in range(100)]  #makes a list of items how ever long the range is
    ylist=[]    # a list incase theres mutliple occurences in the list
    found = False
    search = int(input('Enter an integer: '))   # asks the user what to search for
    for y in range(len(nlist)):         # loops for whole list
        if search == nlist[y]:
            found = True
            ylist.append(y)     # adds the position of the term found to the list of positions
    if found == True:
        ylen = len(ylist)   # the number of terms in ylist is how many times the term was found
        print(f'Found item {ylen} times.')
        print(f'Found item at positions {ylist}.')
    else:
        print('Not found.')
def Bin():
    nlist = [1, 10, 12, 14, 20, 39, 47, 65, 73, 99]    # lsit of items
    found = False
    first = 0
    count = 0
    last = len(nlist)-1    # gets the last position
    search = int(input('Enter an integer: '))
    while found == False and first<=last:  # loops till found or till cant find
        count+=1
        mid = (first+last)//2  # finds the mid point
        if search == nlist[mid]:
            found = True
        elif search > nlist[mid]:
            first = mid+1   # set the first point so the chuck its searching is smaller
        elif search < nlist[mid]:
            last = mid-1    # set the last point so the chunk its searching is smaller
    if found:
        print('The data item has been found.')
        print(f'It took {count} tries.')
    else:
        print('Not found.')

def main():
    SType = int(input('Basic linear(1), Adv linear(2), Binary(3). '))
    if SType == 1:
        BLin()
    elif SType == 2:
        ALin()
    elif SType == 3:
        Bin()
    else:
        print('Pick one of the three')
        main()

if __name__ == '__main__':
    main()
