tempo = int(input("Quantos meses voce trbalhou ?: "))
salario = float(input("Qual o seu salario mensal ?: "))

if tempo >= 12:
    fgts = tempo * salario
    multa = fgts * (40/100)
    print('*' *20) 
    print(f"Voce trabalhou {tempo}")
    print('*' *20) 
    print(f"Voce possui no seu fgts R$ {fgts:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print('*' *20) 
    print(f"A multa de 40% em do valor do seu fgts será de: R$ {multa:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print('*' *20) 


else:
    fgts = tempo * salario
    print('*' *20) 
    print(f"Voce trabalhou {tempo}")
    print('*' *20) 
    print(f"Voce possui no seu fgts R$ {fgts:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print('*' *20) 
    print("Você nao tem direito a receber multa sobre seu fgts")
    print('*' *20) 
