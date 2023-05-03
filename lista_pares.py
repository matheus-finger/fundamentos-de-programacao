# código que mostra a raíz quadrada dos números pares entre 0 e 99
lista = [x**2 for x in range(100) if x % 2 == 0]
print(lista[0:10])