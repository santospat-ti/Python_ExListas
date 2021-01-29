"""Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor."""

num = []
soma = 0

for n in range(10):
    num.append(int(input('Digite um número: ')))
    soma += (num[len(num) - 1] ** 2)
print('A soma dos quadrados do vetor são', soma)