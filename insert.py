def insertion():
    import random, time
    start = time.time()
    items = [random.randrange(1,100) for x in range(100000)]
    len_items = len(items)
    for index in range (1, len_items):
        current = items[index]
        index2 = index
        while index2 > 0 and items[index2-1] > current:
            items[index2] = items[index2-1]
            index2 = index2-1
        items[index] = current
    finish = time.time()
    print(items)
    print('Insertion sort:')
    print('Time taken: ', round((finish - start), 5), ' seconds')

def buble():
    import random, time
    start = time.time()
    items = [random.randrange(1,100) for x in range(100000)] # list of items
    n= len(items)-1 # gets the list's length
    swapped = True
    print(f'The unsorted list is: {items}')
    while swapped and n>0:       # loops the sort
        swapped = False
        for index in range(0, n):   # sets the index across the loops so that it increases each time
            if items[index] > items[index+1]: # checks if the item is bigger than the one to the right
                temp = items[index] # saves the original item
                items[index] = items[index+1] # sets the item to the one on the right of it
                items[index+1] = temp # sets the original to the space on the right
                swapped = True  
        n-=1
    print(f'The sorted list it: {items}')
    end = time.time()
    speed = round(end-start, 5)
    print('Bubble sort:')
    print(f'Time taken: {speed}')


insertion()
buble()
