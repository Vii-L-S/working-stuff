file = open('HW.txt')
content1=file.read()
print(content1)
file = open('HW.txt')
content2=file.readlines()
x=input('What game? ')
v=x
file = open('HW.txt')
mlist= []
hslist= []
for y in content2:
    line =file.readline()
    if x in line:
        mlist.append(line)
        line = line.split()
        hslist.append(line[2])
print(mlist)
hs=max(hslist)
print(f'The highest score in {v} is {hs}.')
print('Thank you for checking the leaderboard')
