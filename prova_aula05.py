from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
soma = reduce(lambda x, y: x + y, numeros)

print("Lista de quadrados:", quadrados)
print("Lista de números pares:", pares)
print("Soma dos números:", soma)
