while True: 
    numero = int(input("Quer ver a tabuada de qual valor ?: "))
    print("_"*30) 
    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}")
    print("_"*45) 
    if numero <= 0:
        print("O valor é menor que 0 por tanto nao pode ser multiplicado")
        print("Fim do Programa")
        break
