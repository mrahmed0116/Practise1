
x = [1,1,4,2,3,4,5,6,8,10,10,10,2,3,5]
y = str(x)
print(y)
for z in y:
    if z.isnumeric():
        print(z)
    else:
        print('Not numeric')
'''
y= [11,12,14,15,18,20]
target= 29
absdiff=[]
coupdigits=[]
for i in x:
    for j in y:
        list1=[i,j]
        coupdigits.append(list1)
        absdiff.append(abs(target-(i+j)))

mi= min(absdiff)
final_index=[]
for a,num in enumerate(absdiff):
    if num ==mi:
        final_index.append(a)
output=[]
for b in final_index:
    output.append(coupdigits[b])
print(output)

s = 'A man, a Plan, a Canal: Panama'
s1=s.lower()
letters=[]
for i in s1:
    if i.isalpha():
        letters.append(i)
if letters ==letters[::-1]:
    print(True)
else:
    print(False)

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


s1= ['hello','world', 'listen to me','', 'hell with you','','wor anbotan','listening to music', 'Janet', '']
s2=sorted(s1)
print(s2)

pre={'empty':0}
for s in s1:
    if len(s)>0:
        if s[0:3] not in pre:
            pre[s[0:3]]=1
        elif s[0:3] in pre:
            pre[s[0:3]] +=1
    else:
        pre['empty'] = pre['empty']+1
print(pre)



dict1= {'x':4,'y':3,'z':2,'a':1,'b':1, 'c':0}
s1 = sorted(dict1.keys(), reverse=True)
print(s1)
output={}
for s in s1:
    for i in dict1:
        if i == s:
            output[i] = dict1[i]

print(output)
'''