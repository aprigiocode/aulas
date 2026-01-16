salario = int(input("Qual o valor do seu salario ?: "))
casa = int(input("Qual o valor da casa ?: "))
tempo = int(input("Em Quantos Anos Voce ira pagar a casa ?: "))
parcela = casa / tempo 

if parcela <= salario * (30/100):
    print("="*20)
    print(f" Salario: R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print("="*20)
    print(f"Valor da casa: {casa:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print("="*20)
    print(f"Parcelas: {tempo}")
    print("="*20)
    print(f"O valor da parcela sera de: R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print("="*20)
else:
    maximo = salario * (30/100)
    print("Para parcelar a casa o valor maixmo de cada parcela nao pode exceder 30% do seu salario")
    print(f"Que seria: R$ {maximo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Voce nao pode parcelar essa casa em {tempo}x pois execede 30% do seu salario que é de R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print("="*45)


