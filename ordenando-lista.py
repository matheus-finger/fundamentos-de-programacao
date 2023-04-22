# importando função randint da biblioteca random, a qual retorna um número inteiro aleatório
from random import randint

# criando a lista desorganizada
lista = []

# fazendo um for para preencher minha lista com 20 números inteiros aleatórios de 0 a 100
for i in range(0, 20):
    lista.append(randint(0, 100))

# mostrando a lista desorganizada
print(lista)

# Esse for irá percorrer a lista
for i in range(0, len(lista)):
    
    # Para cada índice da lista, ele vai primeiro começar da hipótese que o primeiro item é o menor
    menor = lista[i]
    indice_menor = i

    # E então ele vai percorrer o resto da lista para conferir se há um númeno menor que ele
    for j in range (i+1, len(lista)):
        # Se houver um número menor que ele, ele vai armazenar esse número
        if lista[j] < menor:
            menor = lista[j]
            indice_menor = j
    
    # Ele então irá guardar o número atual na posição do menor numero e irá colocar o menor número
    # na posição do número atual e continuar fazendo a mesma coisa para os próximos números
    lista[indice_menor] = lista[i]
    lista[i] = menor

# mostrando a lista organizada
print(lista)