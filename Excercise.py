list1 = ['1','2','2','3','4','4', '5','5', '6','6']
dict1={}
for x in list1:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] +=1

print(dict1)
y=max(dict1.values())
result=[]
for x in dict1:
    if dict1[x] == y:
        result.append(x)

print(result)