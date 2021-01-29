#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas_lista = []

for n in range(4):
    notas_lista.append(float(input(f'Digite a {n + 1}º nota: ')))
    
media = sum(notas_lista) / len(notas_lista)
print('Suas notas foram', notas_lista)
print('Sua média é', round(media, 2))