# O professor quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
nome1 = input('Digite o nome do aluno: ')
nome2 = input('Digite o nome do aluno: ')
nome3 = input('Digite o nome do aluno: ')
nome4 = input('Digite o nome do aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print(f'A sequência de apresentações é: {lista}')


