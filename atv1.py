# $10 A hora trbalhada 
tempo = int(input('Quatas horas voce trabalhou essa semana ?: '))

print(f"Quantidade de horas trabalhas: {tempo}")
print('*' *10)  

print("Valor por hora normal: $10")
print('*' *10)  

if tempo > 44:
    extra2 = tempo - 44         # Quantidade de horas extras
    print(f"Quantidade de horas extras: {extra2}")
    print('*' *10)  
    extra = (extra2 * 15)
    print(f"Hora extra a receber: {extra} (sendo $15 cada hora)")
    print('*' *10)  

else: 
    print(f"Quantidade de horas extras: 0")
    print('*' *10)  
    print(f"Hora extra a receber: 0")
    print('*' *10)  
    print("Voce nao tem horas extras esse mês!")
    print('*' *10)  
