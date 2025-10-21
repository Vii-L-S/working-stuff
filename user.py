
def user():
    global fn
    global ln
    fn = input('Enter your firstname: ')
    ln = input('Enter your lastname: ')
    fn = list(fn) # separates the word into a list of letters
    fn = fn[0] # takes the first letter in the list
    user = ln+fn+'1' # combines the srtings
    return user
    
userlist = []
def existingUsers():
    x=1
    global fn
    global ln
    global userlist
    p = user()
    if p in userlist:
        v = False
    else:
        v = True
        userlist.insert(0, p)   #checks for the user in the list
    while v == False:
        x=x+1
        p =ln+fn+str(x)     #adds a one to the number at the end if already exists
        if p in userlist:
            v = False
        else:
            v = True
            userlist.insert(0, p)
    return p

def main():
    print (existingUsers())

while True:     #runs indefinately to allow for mutliple username entries to check duplicates
    if __name__ == '__main__':
        main()
