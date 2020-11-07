'''
OS funtions and to use them for file manipulation - file size determination
'''

import os
os.chdir('C:\Train\PIC')
byte_size= {'K':1000,'M':1000*1000,'G':1000*1000*1000}
file_list={}
for i in os.listdir():
    if os.path.isfile(i):
        file_list[i] = os.stat(i).st_size

print(file_list)
