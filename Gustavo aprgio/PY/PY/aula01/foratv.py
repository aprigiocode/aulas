palavra = str(input('digite uma palavra: '))
qtd2 = 0
qtd = 0
print(f'a palavra é {palavra}')

for letra in palavra:
    # if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    #     qtd += 1
    --------------------------------------------------------------------------------------------------
    # elif letra == 'e':
    #     qtd += 1
    # elif letra == 'i':
    #     qtd += 1
    # elif letra == 'o':
    #     qtd += 1
    # elif letra == 'u':
    #     qtd += 1

# for letra in palavra:
    if letra in ('a','e','i','o','u'):
        qtd += 1
    else: 
        qtd2 += 1

print (f'a quantidade de vogais é {qtd}')
print (f'e a quantidade de consoates é {qtd2}')
print ('Fim do programa')
