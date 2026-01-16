import random 

jogador1 = ["pedra", "papel", "tesoura"]
escolha1 = random.choice(jogador1)

jogador2 = str(input("Escolha pedra, papel ou tesoura: "))
print(f"Jogador 1 escolheu: {escolha1}")
print("="*20)
print(f"Voce escolheu: {jogador2}")
print("="*20)
    #PAPEL
    
if escolha1 == "papel" and jogador2 == "papel":
    print("Empate")
    print("="*20)
    
elif escolha1 == "papel" and jogador2 == "pedra":
    print(f"Vencedor: {escolha1}")
    print("="*20)
    
elif escolha1 == "papel" and jogador2 == "tesoura":
    print(f"Vencedor: {jogador2}")
    print("="*20)
    #PEDRA
    
elif escolha1 == "pedra" and jogador2 == "pedra":
    print(f"Empate")
    print("="*20)

elif escolha1 == "pedra" and jogador2 == "tesoura":
    print(f"Vencedor: {escolha1}")
    print("="*20)

elif escolha1 == "pedra" and jogador2 == "papel":
    print(f"Vencedor: {jogador2}")
    print("="*20)

        #TESOURA

elif escolha1 == "tesoura" and jogador2 == "pedra":
    print(f"Vencedor: {jogador2}")
    print("="*20)

elif escolha1 == "tesoura" and jogador2 == "papel":
    print(f"Vencedor: {escolha1}")
    print("="*20)

elif escolha1 == "tesoura" and jogador2 == "tesoura":
    print("Empate")
    print("="*20)

else:
    print(f"Vencedor: {jogador2}")
    print("="*20)