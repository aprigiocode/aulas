soma = 0
contador = 0
qtd = int(input('digite a quantidade de numeros que deseja somar: '))

while contador < qtd:
    num = int(input('digte os numeros que deseja somar: '))
    soma += num
    contador += 1
    
print(f'o resultado é : {soma}')