a = 1

def aumenta(a):
    a+=1
    print('No aumenta, a vale', a)

# aqui vai printar a variável que ta dentro do escopo da função,
# não vai alterar a variávei que ta fora da função
aumenta(a)
# aqui ele vai printar a variável que ta fora do escopo, inalterada.
print('Fora do aumenta, a vale', a)

def diminui(a):
    # isso aqui só pode ser executado dentro da minha função,
    # se eu chamar diminui_mais fora da função, ele não
    # achar a função.
    def diminui_mais(a):
        a -= 10
        print('No diminui_mais, a vale', a)
    a -= 2
    print("No diminui, a vale", a)
    diminui_mais(a)

diminui(a)
print('Fora do diminui, a vale', a)

# se eu quiser alterar a variável que ta fora da função,
# posso usar a palavra reservada global, mas isso não é
# recomendado, porque dá muita dor de cabeça quando
# você importa muita biblioteca.

def mult_3():
    global a
    a *= 3
    print("No mult_3, a vale", a)

mult_3()
print('Fora do mult_3, a foi alterada para', a)

# Na prática, geralmente não se usa variáveis globais,
# às vezes se usam constantes (como endereços IP).
# A maioria das vezes somente são criadas variáveis
# locais em funções.
# Além disso, também não são criadas funções dentro de
# funções, como o diminui_mais dentro do diminui. O mais
# comum seria criar duas funções diferentes e chamar
# uma dentro da outra, pois é possível.

# Por padrão, funções que começam com dois underlines
# são funções que não é ideal mexer no código dela,
# pois isso iria trazer complicações.
def __ai():
    print('ai')

__ai