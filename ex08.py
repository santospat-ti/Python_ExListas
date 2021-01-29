"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

lista = []
mult = 1
for n in range(5):
    num = int(input(f'Digite o {n + 1}º número: '))
    lista.append(num)
    mult *= num
    
s = sum(lista)
print('A soma dos vetores é', s)
print('O produto dos vetores é', mult)
print('Os vetores são', lista)
