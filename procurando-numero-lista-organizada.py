
# importando função randint da biblioteca random, a qual retorna um número inteiro aleatório

from random import randint

# criando lista organizada
lista = [0, 12, 21, 30, 45, 64, 67, 82, 90, 95]

# criando um número aleatório para ele procurar entre 0 e 100 e mostrando o número que ele vai procurar
numero = randint(0, 100)
print(numero)

# Obs.: O objetivo desse programa é procurar o número sem ter que percorrer a lista inteira.
# Para isso ele sempre vai procurar o número no meio da lista, se o número procurado é maior que o
# número do meio, então o programa divide a lista em dois e procura pelo número na parte
# da direita, na parte da direita ele vai procurar pelo numero do meio, e vai fazer o mesmo processo.
# Caso o número do meio seja maior que o número que estamos procurando, ele divide a lista em dois e
# procura na parte da esquerda.
# EX.: Estou procurando o número 7 na lista [1, 2, 3, 4, 6, 8, 9, 10, 11]
# O número do meio é o número 6, que é menor que o número 7, então ele divide a lista em duas
# e procura na parte da direita ([8, 9, 10, 11]). Agora ele irá procurar o número do meio de novo.
# No caso, os números do meio são 9 e 10, pois a lista é par, e o programa que eu fiz sempre escolhe
# o número menor dos dois, que é o número 9. O número 9 é maior que 7, logo o programa irá dividir
# a lista em dois ([8] e [10, 11]) e procurar pelo número número da parte da esquerda [8].
# Como a lista só tem um número, ele compara com esse número. 7 é diferente de 8, logo o programa
# irá exibir que não foi possível encontrar o número na lista.

fim = len(lista)-1
inicio = 0

# Esse while aqui testa uma condição que sempre é verdadeira basicamente,
# só saí quando encontra um break
while inicio <= fim:
    # se a lista tiver só um elemento, ele vai comparar se é igual ou não
    if fim - inicio == 0:
        if numero == lista[inicio]:
            print("Achou")
            break
        else:
            print("Não achou")
            break
    else:
        # dividindo a lista no meio (se for par, ela pega o menor número)
        meio = inicio + ((fim - inicio) // 2)
        # checando se o elemento do meio é o número que estamos procurando
        if numero == lista[meio]:
            print("Achou.")
            break
        # se for o numero for maior, ele vai fazer a próxima iteração contando
        # o início como se fosse um numero após o número do meio
        elif numero > lista[meio]:
            inicio = meio + 1
        else:
            # se o número for menor e chegamos ao ""início"" da lista (entre aspas porque
            # o início da lista aqui na verdade é a variável de inicio),
            # quer dizer que o número não foi encontrado
            if inicio == meio:
                print('Não achou')
                break
            # se o número for menor e não estivermos no início da lista,
            # o programa vai contar como se o fim da lista fosse o número
            # logo antes do meio.
            else:
                fim = meio - 1