pessoas = {}

while True:
    nome = input('Digite o nome da pessoa: ')
    idade = input(f'Digite a idade de {nome}: ')

    pessoas[idade] = nome

    cond = input('Deseja continuar a adicionar pessoas ? digite (S) para sim e (N) para nao: ')

    if cond.upper() == 'N':
        break

for nome, idade in pessoas.items():
    print(f'-{nome} {idade}')