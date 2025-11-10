soma = 0
qtd = int(input('digite quantas notas quer somar: '))

for n in range(qtd):
	nota = float(input(f'Digite a {n + 1}ª nota: '))
	soma += nota
	
media = soma / qtd
print(f'A média das notas é {media:.2f}')