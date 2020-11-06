'''
To determine if a number is palindrome or not
'''
num=int(input('Enter a number'))
if num>10:
    num_str = str(num)
    num_str[::-1]
if num_str == str(num):
    print('True')
else:
    print('False')


'''
Without using string functions
'''
num1= num
if num <10 and num>0:
    print('True')
elif num>=10:
    x=0
    while num//10>0:
        x = 10*x+ num%10
        num = num//10
    x = 10 * x + num % 10
    if x == num1:
        print('True')
    else:
        print('False')