'''
Given a list of numbers, find the average of subsequent number in list
if list =[1,2,3,4]
average = [1.5,2.5,3.5]
'''

numbers=input("number")
list1=[int(y) for y in numbers]
list2=[]
for x in range (0, len(list1)-1):
    z=(list1[x]+list1[x+1])/2
    list2.append(z)
print(list2)