'''
Check if target given can be formed by both Small and big (small unit= 1 and big unit = 5)
'''

target = int(input('Enter Target'))
x = int(input('enter small'))
y = int(input('enter big'))

if target > (5*y)+x:
    print(False)
elif target%5 >x:
    print(False)
elif y==0:
    if target > x:
        print(False)
    else:
        print(True)
else:
    print(True)