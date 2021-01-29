"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

listaNotas = []
notasAluno = []
print ('Notas dos Alunos')
for i in range(10):
 	media = 0
 	notasAluno = []
 	print ('Aluno: ' + str(i + 1))
 	for j in range(4):
 		notasAluno.append(float(input('Nota: ' + str(j+1) + '\n')))
 		media += notasAluno[j]
 		print (media)
 	media = media/4
 	listaNotas.append(media)

print (listaNotas)

