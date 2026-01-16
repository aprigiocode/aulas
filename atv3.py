salario = int(input("Qual o valor do salario ?:"))

atraso = int(input("Quantos dias voce atrasou o pagamento ?: "))


if atraso > 5:
    multa = salario * (2/100)
    atraso2 = atraso - 5
    total = multa * atraso2
    total2 = total + salario
    print('*' *20) 
    print(f"Salário: R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print('*' *20) 
    print(f"Dias de atraso: {atraso2}")
    print('*' *20) 
    print("Multa 2% do salario por dia")
    print('*' *20) 
    print(f"Valor da multa R$ {total:.2f}")
    print('*' *20)  
    print(f"Total do salario com a multa é de: R$ {total2:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

else:
    print("Voce nao atrasou o pagamento!!")