'''
Given a String of Parenthesis, Check if it is Valid or not.
New version using Stacks
'''

def find(str1):
    temp = {'(': ')', '{': '}', '[': ']'}
    l = []
    for s in str1:
        if s in temp:
            l.append(s)
        else:
            if not l:
                return False
            if temp[s] != s:
                return False
            l.pop()
    return True

s1= "{[([]{}())}"
print(find(s1))