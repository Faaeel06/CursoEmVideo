# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))

print(f'O Aluno {nome}.\nObteve média {(nota1+nota2)/2} ao final do período!')
