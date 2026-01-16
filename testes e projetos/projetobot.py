# calculador 
numeros = []
contador = 1

def soma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

def sub(numeros):
    total = numeros[0]
    for n in numeros[1:]:
        total -= n
    return total

def mult(numeros):
    total = 1
    for n in numeros:
        total *= n
    return total

def div(numeros):
    total = numeros[0]
    for n in numeros[1:]:
        total /= n
    return total

acao = input("Digite a operação (+ - * /): ")


while True:
    n = int(input(f"Digite o {contador}° número: "))
    numeros.append(n)
    contador += 1

    opcao = input("Deseja adicionar outro número? (s/n): ").lower()
    if opcao != "s":
        acao = input("Digite a operação (+ - * /): ")
        break 
    
    


if acao == "+":
    resultado = soma(numeros)

elif acao == "-":
    resultado = sub(numeros)

elif acao == "*":
    resultado = mult(numeros)

elif acao == "/":
    resultado = div(numeros)

else:
    print("Operação inválida!")
    exit()

print("Resultado:", resultado)




