#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for n in range(6):
    lista.append(int(input(f'Digite o {n + 1}º número: ')))
print(lista)