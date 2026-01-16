salario = float(input("Qual o seu salario mensal ?: "))

meses = int(input('Quantos meses voce trabalhou ?: '))

if meses < 12:
    pagar = salario * (1/12)
    total = pagar * meses 
    print('*' *20) 
    print(f"Salário: R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print('*' *20) 

    print(f"Meses trabalhados: {meses}")
    print('*' *20)  

    print(f"Férias proporcionais de R$ {total:.2f}")
    print('*' *20)  

else: 
    print('*' *20) 
    print(f"Salário: R${salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print('*' *20) 

    print(f"Meses trabalhados: {meses}")
    print('*' *20)  

    print("Voce nao possui ferias proporcionais ")
    print('*' *20)
