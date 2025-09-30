import login

U=input('Please enter Username. ')
P=input('Please enter Password. ')
if U==user and P==password:
    print ('Login Successful')
elif U==user and P!=password:
    print ('Wrong Password')
elif U!=user:
    Print ('Wrong Username')
