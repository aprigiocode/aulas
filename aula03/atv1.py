frutas = {
    "maca": 10,
    "kiwi": 23,
    "pera": 45
}

print(f'o preco da maca é: R${frutas["maca"]}')

frutas["banana"] = 5

print(frutas)

frutas["kiwi"] = 10

print(frutas)

for fruta, preco in frutas.items():
        print(f'{fruta}: R${preco}')