def p():
    p = int(input('What is the princible amount? '))
    return p
def t():
    t = int(input('How many years has it been? '))
    return t
def r():
    r = int(input('What is the rate? '))
    return r
def main():
    i =( p()*r()*t() )/100
    print (i)

if __name__ == '__main__':
    main()
