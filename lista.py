
lista = []
for x in range(20):
    lista.append(x**2)
print(lista)
# quero tirar o elemento 169 se
# mais legível que range
for i, valor in enumerate(lista):
    if valor == 169:
        lista.pop(i)

# isso também pode ser feito com a função remove de uma variável de lista