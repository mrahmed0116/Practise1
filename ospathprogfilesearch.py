'''
OS funtions and to use them for file manipulation - file search using prefix
'''

import os
pref = input('prefix to be found')
os.chdir('C:\Train\PIC')
file_list=[]
for i in os.listdir():
    if os.path.isfile(i):
        j=i.lower()
        if j[0:len(pref)] == pref:
            file_list.append(i)
print(file_list)