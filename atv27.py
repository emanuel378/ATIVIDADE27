# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria


lista = []
for co in range(7):
    convidado = input(f"Digite o convidado {co+1}:")

    lista.append(convidado)
sn = input("Deseja remove algum convidado? (sim/não)")
if sn == "sim":
        qual=input("Digite o nome do convidado:")
        lista.remove(qual)
        print(lista)
else:
    print("blz")
