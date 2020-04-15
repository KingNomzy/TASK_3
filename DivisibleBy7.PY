num = []
for n in range(1500, 2700):
    if(n%7==0) and (n%5==0):
        num.append(str(n))
print(' ')
print(','.join(num))

age =input('enter your age sir \n')
print (f'are u really {age} years old?')
