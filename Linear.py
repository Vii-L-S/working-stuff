import random
listd = [random.randrange(1,100) for x in range(1000)]  #makes a list of 1000 random numbers
ylist= []
def main():
    found = False
    search = int(input('Enter a number: '))     # get the term to search for
    for y in range(len(listd)):     #loops the search
        if search ==listd[y]:
            found = True
            ylist.append(y)     # adds the position to a list incase its in the original list multiple times
    if found == True:
        ylen = len(ylist)   # gets the length of the list to tell how many times it was found
        print(f'Found item {ylen} times')
        print(f'Found item at positions {ylist}.')
    else:
        print('Item not found.')
        
if __name__ == '__main__':
    main()
