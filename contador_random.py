from random import choice

numeros = [1,2,3,4,5,6,7,8,9,10]
counter = []

for j in range(10):
    counter.append(0)
for x in range(10):
    numero_aleatorio = choice(numeros)
    counter[numero_aleatorio-1] += 1
for y in range(10):
    if counter[y] != 0:
        print(f"El número {y+1} ha salido: {counter[y]} veces...")