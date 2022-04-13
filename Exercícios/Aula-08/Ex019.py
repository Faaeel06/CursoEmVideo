# Um professor quer sortear um dos seus alunos quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random

nome1 = input('Digite o nome do aluno: ')
nome2 = input('Digite o nome do aluno: ')
nome3 = input('Digite o nome do aluno: ')
nome4 = input('Digite o nome do aluno: ')
lista = [nome1, nome2, nome3, nome4]
nomes = random.choice(lista)
print(f'O aluno escolhido foi: {nomes}')



