'''
Given 2 Lists and a target. Find how many combinations can be found
'''

x = [1,2,3,4,5,6,8,10]
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