'''
18 - Uma grande emissora de televisão quer fazer uma enquete
entre os seus telespectadores para saber qual o melhor jogador
após cada jogo. Para isto, faz-se necessário o desenvolvimento
de um programa, que será utilizado pelas telefonistas, para a
computação dos votos. Sua equipe foi contratada para desenvolver
este programa, utilizando a linguagem de programação C++.
Para computar cada voto, a telefonista digitará um número,
entre 1 e 23, correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo,
mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida,
juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados
como votos. O resultado aparece ordenado pelo número do jogador.
O programa deve fazer uso de arrays. O programa deverá executar o
cálculo do percentual de cada jogador através de uma função.
Esta função receberá dois parâmetros: o número de votos de um
jogador e o total de votos. A função calculará o percentual e
retornará o valor calculado. Abaixo segue uma tela de exemplo.
O disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa.
Ao final, o programa deve ainda gravar os dados referentes ao
resultado da votação em um arquivo texto no disco,
obedecendo a mesma disposição apresentada na tela.
'''

#vetor com 23 posições, iniciando com o valor zero 
jogadores = [0] * 23
total = 0
print('Enquete: quem foi o melhor jogador? ')
while True:
    while True:
        numero = int(input('Número do jogador (0=fim): '))
        if (numero > 23) or (numero < 0):
            print('Informe um valor entre 1 e 23 ou 0 para sair!')
        else:
            break
    if numero == 0:
        break
    jogadores[numero-1] += 1
    total += 1

    
print('\nResultado da votação: ')
print(f'Foram computados {sum(jogadores)} votos.')
contador = 1
melhorJogador = 0

for j in jogadores:
    print(f'\nJogador {contador} - votos: {j}')
    if j > 0:
        print(f'\t{contador}, \t{j}, \t{round(j / float(total) * 100)}%')
    if j > jogadores[melhorJogador]:
        melhorJogador = contador - 1
    contador += 1

   
print(f'Melhor jogador foi o número {melhorJogador + 1} com {jogadores[melhorJogador]} votos.')
print(f'Percentual: {round(jogadores[melhorJogador] / float(total) *100)}%.')