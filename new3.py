def isValid(s):
    if len(s) % 2 != 0:
        return False
    else:
        list1 = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                list1.append(x)
                print(list1)
            if x == ')':
                if list1[-1] == "(":
                    del list1[-1]
                    print(list1)
                else:
                    return False
            elif x == "}":
                if list1[-1] == "{":
                    del list1[-1]
                    print(list1)
                else:
                    return False
            elif x == "]":
                if list1[-1] == "[":
                    del list1[-1]
                    print(list1)
    print(list1)
    if list1 == []:
        return True
    else:
        return False

s1= "{[([]{}())]}"
print(isValid(s1))