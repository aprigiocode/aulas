pessoas = [
{"nome": "Gustavo", "sexo": "M", "idade":22}
]
for k,v in pessoas():
    print(f"{k} = {v}")
    mudar = ("Deseja mudar algum nome da lista [S/N] ?: ").upper
    if mudar == "S":
        escolha = input("Qual Nome Deseja Mudar ?: ")
        novo_nome = input("Qual Sera o Novo Nome ?:")
        