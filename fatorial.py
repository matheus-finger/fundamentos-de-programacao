# fatorial: identificador da função
# m: parâmetro
# return: retorna o valor da expressão à direita (no caso o r)

def fatorial(m):
    r = 1
    for i in range(1, m+1):
        r *= 1
    return r

# chamando a função
# 3 é o argumento
fatorial(3)