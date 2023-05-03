vogais = ['A', 'E', 'I', 'O', 'U']
print(len(vogais))
# pega última letra
print(vogais[-5])
# daria erro:
# print(vogais[-6])


copia = vogais
# esse código vai alterar a lista também, porque você na verdade
# não criou uma cópia, mas sim uma variável que se referencia
# a mesma lista, e o tipo lista é mutável.
copia.append(2)
print(vogais)

# Nesse código, você não irá alterar teste, porque o inteiro
# é um valor imutável, logo você cria um novo valor toda
# vez que alterar a variável
teste = 1
copia2 = teste
# aqui a cópia para de apontar pra mesma variável e tem
# o valor alterado, mas teste continua com o mesmo
# valor.
copia2 += 1
print(teste)
