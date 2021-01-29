"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

perguntas = ['Telefonou para a vítima?',
             'Esteve no local do crime?',
             'Mora perto da vítima?',
             'Devia para a vítima?',
             'Já trabalhou com a vítima?']

status = {2 : 'Suspeita',
          3 : 'Cúmplice',
          4 : 'Cúmplice',
          5 : 'Assassino'}
print()
print('\nINTERROGATÓRIO')
print()
veredicto = 0
for p in range(len(perguntas)):
    print(perguntas[p])
    resp = str(input('Digite S para SIM e N para NÃO: ')).upper()
    while resp not in 'SN':
        resp = str(input('\nValor inválido. Digite S para Sim e N para Não.')).upper()
    if resp == 'S':
        veredicto += 1
if veredicto in status:
    print(status[veredicto])
else:
    print('Inocente.')
