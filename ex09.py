"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida."""

lista_idade = []
lista_altura = []
n_pessoa = 1

for p in range(5):
    print('Pessoa', n_pessoa)
    lista_altura.append(float(input('Digite sua altura: ')))
    lista_idade.append(int(input('Digite sua idade: ')))
    n_pessoa += 1

print(lista_idade[::-1])
print(lista_altura[::-1])
