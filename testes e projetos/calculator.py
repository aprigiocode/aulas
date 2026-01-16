def positivo_ou_negativo(numero):
    if numero >= 0:
        print("Positivo")
    else:
        print("Negativo")

numeros = int(input("Digite um numero: "))

resposta = positivo_ou_negativo(numeros)


def contar_vogias(texto: str):
    contador = 0
    for n in texto:
        if n == "a":
            contador += 1
        elif n == "e":
            contador += 1
        elif n == "i":
            contador += 1
        elif n == "o":
            contador += 1
        elif n == "u":
            contador += 1
    return contador

palavras = str(input("Digite uma palavra: "))

vogais = contar_vogias(palavras)

print(f"A quantidade de vogais na palavra é {vogais}")

