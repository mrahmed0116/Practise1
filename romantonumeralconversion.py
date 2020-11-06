'''
Roman to Numeric converter
'''
s="LXI"
Roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
if len(s) > 15 or len(s) < 1:
    print(False)
else:
    list1 = [Roman[s[x]] for x in range(0, len(s))]
    list2=[]
    for x in range(0,len(s)):
        list2.append(Roman[s[x]])
print(list1)
print(list2)