# Os índices tem que ser variáveis imutáveis, como strings e números,
# variáveis mutáveis como listas não podem ser índices.
usuario = {'nome': 'João', 'data_nascimento': '28-07-1980'}


# Diferente de quando você compara listas, em que a ordem dos elementos importe,
# quando você compara dicionários, a ordem dos índices não importe
usuario2 = {'data_nascimento': '28-07-1980', 'nome': 'João'}
if usuario == usuario2:
    print('A ordem não importa')

# não é possível fazer fatiamento de dicionários: usuario[1:2] daria erro

# esse método procura pelo índice número, e se não houver, ele retorna
# o segundo argumento. No caso, S/N.
print(usuario.get('número', 'S/N'))

# Percorrendo o dicionário
for chave, valor in usuario.items():
    print('Chave: ', chave)
    print('Valor: ', valor)