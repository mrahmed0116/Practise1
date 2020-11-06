s1= ['hello','world', 'listen to me','', 'hell with you','','wor anbotan','listening to music', 'Janet', '']
s2=sorted(s1)
print(s2)

pre={'empty':0}
for s in s1:
    if len(s)>0:
        if s[0:3] not in pre:
            pre[s[0:3]]=1
        elif s[0:3] in pre:
            pre[s[0:3]] +=1
    else:
        pre['empty'] = pre['empty']+1
print(pre)
