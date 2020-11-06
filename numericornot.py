'''
Mish mash of Practise questions all rolled in one. Splitting it into different programs
'''
x = [1,1,4,2,3,4,5,6,8,10,10,10,2,3,5]
y = str(x)
print(y)
for z in y:
    if z.isnumeric():
        print(z)
    else:
        print('Not numeric')
