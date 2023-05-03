def lista_quadrada(lista:list):
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2


# como lista é mutável, sempre quando você passar uma lista como argumento, você 
listinha = [1, 2, 3, 4]
print('LISTA INICIAL')
print(listinha)
lista_quadrada(listinha)
lista_quadrada(listinha)

print('lista_quadrada')
print(listinha)


def lista_quadrada2(lista:list):
    copia = lista
    for i in range(len(copia)):
        copia[i] = copia[i] ** 2

# isso aqui também altera, pois você não faz uma
# copia de verdade na função, pois lista
# é uma variável mutável

print('lista_quadrada2')
lista_quadrada2(listinha)
print(listinha)


def lista_raiz(lista:list):
    copia = []
    for i in range(len(lista)):
        copia.append(lista[i] ** 0.5)

# nesse caso, não alterei lista
# pois a nova lista não referencia
# a minha lista
lista_raiz(listinha)

print('lista_raiz')
print(listinha)