

situação = ('1 - Necessita de Esfera', 
            '2 - Necessita de limpeza',
            '3 - Necessita troca do cabo ou conector',
            '4 - Quebrado ou inutilizado')
totalDefeitos = [0] * 4
totalmouses = 0
for i in situação:
    print(i)

while True:
    mouse = int(input('Número de identificação: '))
    if mouse != 0:
        defeito = int(input('Tipo de defeito: '))
        totalDefeitos[defeito - 1] +=1
        totalmouses += 1
        
    if mouse == 0:
        break

print(f'Situação               \tQuantidade          \t Percentual')
for m in range(0, len(situação)):
    print(f'{situação[m]}  \t{totalDefeitos[m]:<10} \t{round(totalDefeitos[m] / float(totalmouses) * 100)}%')