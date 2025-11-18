frutas = {}
ns = int(input('Digite quantas frutas deseja adicionar a lista: '))

for n in range(ns):
    nome = input('digite o nome da fruta: ')
    preço = input(f'digite o valor de {nome}: ')

    frutas[nome] = preço

for nome, preco in frutas.items():
        print(f'{nome}: {preco}')

print(f'a lista de telefones é : {frutas}')