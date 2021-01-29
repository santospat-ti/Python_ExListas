"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos 
com mais de 13 anos possuem altura inferior à média de altura desses alunos."""

lista_idade = [13, 23, 25, 36, 32, 27]
lista_altura = [1.50, 1.36, 1.86, 1.96, 1.50, 1.70]

mediaalt = sum(lista_altura) / len(lista_altura)
n_aluno = 0
for a in range(0, len(lista_idade)):
    if lista_idade[a] > 13 and lista_altura[a] < mediaalt:
        n_aluno += 1

print(n_aluno, 'possuem altura inferior a média de ', round(mediaalt, 2))
