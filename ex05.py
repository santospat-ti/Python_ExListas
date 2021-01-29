"""Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números
pares na listar PAR e os números IMPARES na lista impar. Imprima os três vetores."""

lista_num = []
l_par = []
l_impar = []
num = 0
for n in range(6):
    lista_num.append(int(input(f'Digite o {n + 1}º número:')))
    num = lista_num[n]
    print(num)
    if num % 2 == 0:
        l_par.append(num)
    else:
        l_impar.append(num)
print(lista_num)
print(f'Números pares: {l_par} \nNúmeros ímpares: {l_impar}.')