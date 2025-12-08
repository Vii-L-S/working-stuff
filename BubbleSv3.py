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
print(f'Time taken: {speed}')
