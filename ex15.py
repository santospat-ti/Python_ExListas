"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados 
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""
from time import sleep
valores_lista = []
valores = True
n_valores = 0

while valores != -1:
    print('Valor', n_valores + 1)
    valores = float(input('Digite um valor: '))
    if valores == -1:
        break
    else:
        valores_lista.append(valores)
        n_valores += 1
media = sum(valores_lista) / len(valores_lista)

print(f'Valores lidos: {n_valores}')
print(valores_lista) #lado a lado
print(valores_lista[::-1])
print(f'Soma: {sum(valores_lista)}') #soma
print(f'Média: {round(media, 2)}') #media
valor_acima = 0
abaixo_sete = 0

for v, k in enumerate(valores_lista): 
    if k > media:
        valor_acima += 1
    if k < 7:
        abaixo_sete += 1
print(f'Total de valores acima da média {valor_acima}')
print(f'Total de valores abaixo de sete {abaixo_sete}')
print('Finalizando...')
sleep(2)
print('Programa finalizado!')





