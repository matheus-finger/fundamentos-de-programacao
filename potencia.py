# b é um argumento opcional, com valor default de 2
def pow(a, b=2):
    return a ** b

# só vai executar dentro do if se você executar o arquivo potencia.py,
# e não vai rodar quando você ta usando outro
# arquivo que ta importando potencia
# importante porque as vezes esses testes precisam de muito
# processamento e você não quer que esses testes ocorram
# quando você está querendo somente importar a função pow em
# outro arquivo.
# __name__: nome do arquivo, se você estiver rodando o próprio arquivo
# então o nome vira __main__, quando você executar em outro arquivo,
# nesse if o resultado de __name__ vai ser potencia, e não __main__.
if __name__ == '__main__':
    # verificando se há erros na função
    pass
    assert pow(2, 0) == 1
    assert pow(2, 1) == 2
    assert pow(2, 3) == 8
    assert pow(3, 3) == 27