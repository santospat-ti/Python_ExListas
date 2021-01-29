"""Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20
elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras
listas."""

lista_um = []
lista_dois = []
lista_tres = []
lista_inter = []
for n in range(10):
    print('Lista um')
    lista_um.append(int(input(f'Digite o {n + 1}º elemento: ')))
for c in range(10):
    print('Lista dois')
    lista_dois.append(int(input(f'Digite o {c + 1}º elemento: ')))
for x in range(10):
    print('Lista três')
    lista_tres.append(int(input(f'Digite o {x + 1}º elemento: ')))
for m in range(10):
    lista_inter.append(lista_um[m])
    lista_inter.append(lista_dois[m])
    lista_inter.append(lista_tres[m])
print(lista_um)
print(lista_dois)
print(lista_tres)
print(lista_inter)

