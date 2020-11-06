'''
Given a string. Check if the string is a palindrome
'''

s = 'A man, a Plan, a Canal: Panama'
s1=s.lower()
letters=[]
for i in s1:
    if i.isalpha():
        letters.append(i)
if letters ==letters[::-1]:
    print(True)
else:
    print(False)