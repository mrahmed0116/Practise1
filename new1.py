'''
Given 2 Lists and a target. Find how many combinations can be found
'''

x = [1,2,3,4,5,6,8,10]
y= [11,12,14,15,18,20]
middle_x = (0+len(x))//2
middle_y =(0+len(y))//2
target = 19
highest_x = len(x)
highest_y = len(y)
lowest_x = 0
lowest_y = 0
#print(lowest_x,lowest_y,middle_x,middle_y,highest_x,highest_y)
while highest_x > lowest_x:
    #print('True')
    z= x[middle_x] + y[middle_y]
    #print(z)
    if x[middle_x] + y[middle_y] > target:
        highest_x = middle_x -1
        highest_y = middle_y -1
        middle_x = (lowest_x + highest_x) // 2
        middle_y = (lowest_y + highest_y) // 2
        #print(highest_x,highest_y,middle_y,middle_x)
    elif x[middle_x]+y[middle_y] < target:
        #print(x[middle_x] + y[middle_y])
        lowest_x = middle_x+1
        lowest_y = middle_y
        middle_x = (lowest_x + highest_x) //2
        middle_y = (lowest_y+highest_y) //2
        print(highest_x, highest_y, middle_x, middle_y)
    else:
        break