def proximo_primo(lista:list[int]):
    """
    Procura o próximo número primo e retorna ele
    """
    ultimo = int(lista[len(lista)-1])
    num = ultimo + 1
    while True:
        primo = True
        for i in lista:
            if num % i == 0:
                primo = False
            break
        if primo:
            return num
        num = num + 1

def lista_primos(n:int):
    """
    Retorna os n primeiros primos
    """
    anteriores = [2]
    for i in range(0, n-1):
        novo = proximo_primo(anteriores)
        anteriores.append(novo)
    return anteriores


result = lista_primos(1000)
print(result[0:10])
print(result[990:1001])