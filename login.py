user = 'admin'
pswd = 'passwd'
name = input('Please enter Username: ')
pss = input('Please enter Password: ')
if user == name and pswd == pss:
    print('Login Successfull!!')
elif user == name and pswd != pss:
    print ('Incorrect Password.')
elif user!= name:
    print('Wrong Username.')
