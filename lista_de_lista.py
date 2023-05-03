
# criando uma lista que tem 5 listas, mas todas
# são identicas, e se você alterar uma, você
# altera todas, pois todas são referências
# a mesma lista
lista1 = [[1]]*5
print('Lista inicial')
print(lista1)
lista1[1].append(4)
print('Lista após tentar alterar 1 elemento')
print(lista1)

# agora vamos criar uma lista com 5
# listas diferentes
lista2 = []
for i in range(0, 5):
    lista2.append([1])
print('Lista com elementos diferentes')
print(lista2)
lista2[1].append(4)
print('Tentando alterar um elemento')
print(lista2)