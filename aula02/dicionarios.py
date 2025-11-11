# Exemplo de lista telefônica
# telefones = {
#     "Ana": "9999-1234",
#     "João": "8888-4321",
#     "Maria": "9777-5678"
# }

# print(telefones[1])

telefones = {
    "Ana": "9999-1234",
    "João": "8888-4321",
    "Maria": "9777-5678"
}
for n in range(3):
    nome = input('digite o nome da pessoa: ')
    numero = input('digite o umero da pessoa: ')
    telefones[nome] = numero

print(telefones)