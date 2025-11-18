frutas = {}
# ns = int(input('Digite quantas frutas deseja adicionar a lista: '))

while True: 
    nome = input('digite o nome da fruta: ')
    preço = input(f'digite o valor de {nome}: ')

    frutas[nome] = preço

    resp = input('Deseja colocar mais frutas: [S/N]: ')

    if resp.upper() == 'N':
        break

for nome, preco in frutas.items():
        print(f'O preço da {nome} é: ${preco}')
    
bsc = input('Digite a fruta que deseja procurar: ')

print(frutas.get(bsc))

if frutas.get(bsc) == None:
     add1 = input('Digite o nome da fruta: ')
     add2 = input(f'Digite o valor de {add1}: ')
     frutas[add1] = add2
else: 
    print('A fruta ja existe')


for nome, preco in frutas.items():
        print(f'O preço da {nome} é: ${preco}')