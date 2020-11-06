'''
Add 2 lists and print the highest number
'''

l1=[1,2,3,4,5,6]
l2=[1,2,3,4]
for x in l2:
    l1.append(x)
print(l1)
l1.sort()
print(l1[-1])