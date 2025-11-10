soma = 0
qtd = int(input('digite quantas notas deseja somar: '))

for n in range(qtd):
	nota = float(input('Digite uma nota: '))
	soma += nota
	
media = soma / qtd
print(f'A média das 3 notas é {media:.2f}')