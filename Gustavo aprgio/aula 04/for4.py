num = int(input('digite um numero: '))
num2 = 1

for i in range (1,num, +1):
    print(i, end='*')
    num2 *= i 
print (f'= {num2}')