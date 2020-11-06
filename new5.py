'''
Given a list of strings, find the most common prefix
'''

strs= ["flower","flow","flight","florida","fling","floozie"]
str0 = strs[0]
count=0
list1=[]
for i in range(1, len(str0)):
    if count == (i-1)*len(strs):
        for strng in strs:
            if str0[0:i] in strng:
                count=count+1
                list1.append(str0[0:i])
    else:
        break
x=int(count/len(strs))
print(list1)
print(str0[0:x])
print(x)