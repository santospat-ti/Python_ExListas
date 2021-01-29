"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )"""

temperatura_lista = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for t in range(0, len(meses)):
    temp = float(input(f'Digite a temperatura do mês {t + 1}: '))
    temperatura_lista.append(temp)
media = sum(temperatura_lista) / len(temperatura_lista)
for t in range(0, len(temperatura_lista)):
    if temperatura_lista[t] > media:
        
        print(str(t + 1) + '-' + meses[t])