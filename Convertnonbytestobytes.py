'''
input in MB/GB/TB to bytes
'''

target = input('input target size bytes')
byte_size= {'k':1000, 'm':1000000, 'g':1000000000, 't':1000000000000}
target_new= 0
if target[-1] == 'B':
    x=target[-2].lower()
    if x in byte_size:
        target_new = int(target[:-2]) * byte_size[x]
    else:
        target_new = target
else:
    print('invalid target')
print(target_new)
