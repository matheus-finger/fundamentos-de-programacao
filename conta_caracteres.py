def conta_caracteres(strings: list[str]) -> dict:
    resultado = {}
    for string in strings:
        for caractere in string:
            # ele compara com as chaves por padrão, e não com os valores
            if caractere not in resultado:
                resultado[caractere] = 1
            else:
                resultado[caractere] += 1
    return resultado


if __name__ == '__main__':
    listas = ["abelhinha", "besourinho", "minhoquinha"]
    print(conta_caracteres(listas))