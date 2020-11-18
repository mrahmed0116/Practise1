import os
os.chdir('C:\Train\PIC')

file1 = open('list1.txt', 'r')
Lines = file1.readlines()
entry=[]
city={}
state={}
for i in Lines:
    entry = i.split(',')
    if entry[-1] not in state:
        state[entry[-1]] = 1
    else:
        state[entry[-1]] += 1
    if entry[-2] not in city:
        city[entry[-2]] = 1
    else:
        city[entry[-2]] += 1
print(city)
print(state)