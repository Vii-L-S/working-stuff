def findFirst(Books):
    for z in range(len(Books)):
        if Books[z][2] == '':
            return Books[z][1]
    return -1

def main():
    Books = [
        [1, '09:00', '5877RC'],
        [2, '09:30', '9655AS'],
        [3, '10:00', ''],
        [4, '10:30', '8754TT'],
        [5, '11:00', ''],
        [6, '11:30', '8745SD'],
        [7, '13:00', '9635GH'],
        [8, '13:30', ''],
        [9, '14:00', '9874PL'],
        [10, '14:30', '9658SV']]
    print('The first empty slot is: {}'.format(findFirst(Books)))

if (__name__ == "__main__"):
    main()
