l1=[1,2,3,4,5,6]
l2=[1,2,3,4]
for x in l2:
    l1.append(x)
print(l1)
"""
for x in range(0,len(l1)):
    for y in range (0,len(l1)-1):
        if l1[x]<l1[y+1]:
            l1[x],l1[y+1] = l1[y+1], l1[x]
"""
l1.sort()
print(l1[-1])