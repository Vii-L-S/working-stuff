def linear():
    print('Linear Search: ')
    nlist = [1, 7, 14, 19, 21, 36, 39, 46, 59, 61]
    found = False
    search = int(input('Enter an integer: '))   #gets the integer to look for
    nlen = len(nlist)
    for x in range(0, nlen):    #loops and searches whole list
        if nlist[x] == search:
            found = True
            pos = x+1   #gets the position of the found integer (+1 because lists start at 0)
    if found == True:
        print(f'Found at position {pos}')
    else:
        print('Not found')
def binary():
    print('Binary Search: ')
    nlist = [1, 7, 14, 19, 21, 36, 39, 46, 59, 61]
    count = 0
    first = 0
    mid = 0
    last = len(nlist) -1
    found = False
    search = int(input('Enter an integer: '))
    while found == False and first<=last:
        count +=1
        mid = (first+last)//2
        midA = nlist[mid]       # sets the integer thats at position mid to a variable itself
        if search == midA:
            found = True
            pos = mid+1
        elif midA < search:
            first = mid+1   #Changes first pointer
        elif midA > search:
            last = mid-1    # changes last pointer
    if found == True:
        print(f'Found at position {pos}')
    else:
        print('Not found')
def bubble():
    print ('Bubble Sort:')
    nlist = [1, 14, 7, 19, 21, 36, 46, 39, 59, 61]
    nlen = len(nlist)
    print ('Unsorted list: ', nlist)
    for x in range(nlen):
        for index in range(nlen-1):
            if nlist[index] > nlist[index+1]:
                temp = nlist[index]
                nlist[index] = nlist[index+1]
                nlist[index+1] = temp
    print ('sorted list: ', nlist)
def insertion():
    print ('Insertion Sort:')
    nlist = [1, 14, 7, 19, 21, 36, 46, 39, 59, 61]
    nlen = len(nlist)
    print ('Unsorted list: ', nlist)
           
linear()
binary()
bubble()
insertion()
