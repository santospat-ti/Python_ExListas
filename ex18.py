"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções 
devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual 
de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""

print('Qual o melhor Sistema Operacional para uso em servidores? ')
sistemas_votos = [0] * 6 #vetor com 6 posições, iniciando com valor 0
sistemas_operacionais = ['Windows S.', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
totalVotos = 0

i = 0
for sistema in sistemas_operacionais:
    print(i + 1, sistemas_operacionais[i])
    i += 1

while True:
    while True:
        opcao = int(input('Sistema escolhido (0=fim)'))    
        if opcao > 6 or opcao < 0:
            print('Valor inválido. Digite a opção de 1 a 6. ')
        else: 
            break
    if opcao == 0:
        break
    sistemas_votos[opcao - 1] += 1   
    totalVotos += 1


print('Sistema Operacional     Votos    %')
print('-' * 40)
i = 0
melhor_sistema = 0
for sistema in sistemas_operacionais:
    print(sistemas_operacionais[i], sistemas_votos[i], sistemas_votos[i] / float(totalVotos) * 100)
    
    if (sistemas_votos[i] > sistemas_operacionais[melhor_sistema]):
        melhor_sistema = i        
    i += 1
print('-' * 40)
print('Total', sum(sistemas_operacionais), totalVotos)
print(f'O Sistema Operacional mais votado foi o {sistemas_operacionais[melhor_sistema]}, com {sistemas_votos[melhor_sistema]} votos.')
print(f'Percentual: {sistemas_votos[melhor_sistema] / float(totalVotos) * 100}%.')