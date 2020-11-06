import os
os.chdir('C:\Train\PIC')
byte_size= {'K':1024,'M':1024*1024,'G':1024*1024*1024}
target = '600GB'
target_new= 0
if target[-1] == 'B':
    if target[-2] in byte_size:
        target_new = int(target[:-2]) * byte_size[target[-2]]
    else:
        target_new = target
else:
    print('invalid target')
print(target_new)
file_list={}
subdirectory1={}
nosubdir = True
while nosubdir == True:
    for i in os.listdir():
        if os.path.isfile(i):
            file_list[i] = os.stat(i).st_size
        elif os.path.isdir(i):
            subdirectory1[i] = os.listdir(i)
            if os.listdir(i) == []:
                nosub = False

print(file_list)