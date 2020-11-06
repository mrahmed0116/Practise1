prime_numbers=[]
for x in range (2,100):
    count=0
    for y in range (2,x):
        if x%y == 0:
            count=count+1
    if count==0:
        prime_numbers.append(x)
print(prime_numbers)

prime_numbers1 = [x for x in range(2, 100) if all(x % i != 0 for i in range(2, x - 1))]
print(prime_numbers1)