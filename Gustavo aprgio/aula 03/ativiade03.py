numero1 = int(input('digite dois numeros de 1 a 10: '))
numero2 = int(input('digite dois numeros de 1 a 10: '))
if numero1 == numero2:
    print('os numeros sao iguais')
elif numero1 > numero2:
    print (f'o {numero1} é maior que o {numero2}')
elif numero1 < numero2:
    print (f'o {numero2} é maior que o {numero1}')