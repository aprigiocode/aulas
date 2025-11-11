pares = []
impares = []


for n in range(10):
	numero = int(input('Digite um numero: '))

	if numero % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)
      

print(f'A lista de pares é: {pares} e a lista de impares é: {impares}')