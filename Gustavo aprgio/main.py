despesa = []

while True:
    print("=" * 30)
    print("Gerenciador de Despesas")
    print("=" * 30)
    print("[1] - Listar Despesas")
    print("[2] - Cadastrar Despesas")
    print("[3] - Editar Despesa")
    print("[4] - Excluir Despesa")
    print("[5] - Sair")
    print("=" * 30)
    opcao = int(input("Opção: "))

    if opcao == 1:
        for lista in despesa:
            print("=" * 30)
            print(f" - {lista['titulo']}")
            print(f"valor: R${lista['valor']}")
            print(f"descricao: {lista['descricao']}")
            print("=" * 30)

    elif opcao == 2:
            titulo = input("Digite o nome da Despesa: ")
            valor = input("Digite o valor da Despesa: ")
            descricao = input("Digite a descrição da Despesa: ")
            despesa.append({
                "titulo": titulo,
                "valor": valor,
                "descricao": descricao
                 })
            
    elif opcao == 3:
        for i, lista in enumerate(despesa):
            print(f"[{i}] {lista['titulo']} - R$ {lista['valor']}")
        indice = int(input("Digite a despesa que deseja alterar: "))
        lista = despesa[indice]
        lista["titulo"] = input("Novo título: ")
        lista["valor"] = input("Novo valor: ")
        lista["descricao"] = input("Nova descrição: ")
        print("Despesa editada com sucesso!")
    
    elif opcao == 4:
        for i, lista in enumerate(despesa):
            print(f"[{i}] {lista['titulo']} - R$ {lista['valor']}")
        indice2 = int(input("Digite a despesa que deseja excluir: "))
        lista = despesa.pop(indice2)


    else:
         print("Fim do Programa!")
         break