qtd = int(input('digite quantas frutas deseja adicionar: '))
frutas = []

for n in range(qtd):
	fruta = (input('Digite uma fruta: '))
	frutas.append(fruta)
# print(f'As frutas sao {frutas}')

print('Frutas: ')
for fruta in frutas:
	print(f'- {fruta}')