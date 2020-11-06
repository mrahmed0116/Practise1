'''
Sort dictionary based on keys
'''

dict1= {'x':4,'y':3,'z':2,'a':1,'b':1, 'c':0}
s1 = sorted(dict1.keys())
print(s1)
output={}
for s in s1:
    for i in dict1:
        if i == s:
            output[i] = dict1[i]

print(output)

'''
Sort dictionary based on values
'''
s2 = sorted(dict1.values())
print(s2)
output1={}
for j in s2:
    for i in dict1:
        if j == dict1[i]:
            output1[i] = dict1[i]

print(output1)