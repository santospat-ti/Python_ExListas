#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
for n in range(10):
    lista.append(float(input(f'Digite o {n + 1}º número: ')))
    lista.sort(reverse=True)
print(f'{lista}')