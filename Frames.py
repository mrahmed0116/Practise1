frames = ['1','3','5','9','10']
n,w,h = input().split(" ")
area= int(n)*int(w)*int(h)
print(area)
lx= 0
rx = len(frames)
flag = 0
lx1=0
rx1=0
while lx<=rx:
    middle= (lx+rx) //2
    print(str(middle) + 'Middle in loop')
    if int(frames[middle]) * int(frames[middle]) < area:
        print(int(frames[middle]) * int(frames[middle]))
        lx = middle
        lx1 = 1
        if rx1==1:
            middle= middle+1
            break
    elif int(frames[middle]) * int(frames[middle]) > area:
        print(int(frames[middle]) * int(frames[middle]))
        rx = middle
        rx1=1
        if lx1==1:
            break
    elif int(frames[middle]) ** int(frames[middle]) == area:
        break
print(int(middle))