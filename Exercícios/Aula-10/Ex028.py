# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
import time

print('-=-' * 15)
print('=' * 5, 'Vamos jogar um jogo?', '=' * 5)
time.sleep(0.5)
print('Vou pensar em um número, tente advinhar')
time.sleep(0.5)
print('Pensando...')
time.sleep(1)
computador = random.randint(0, 5)
usuario = int(input('Digite sua opção entre 1 e 5: '))
if usuario == computador:
    print('Você acertou! Parabéns!')
else:
    print('Que pena! Você errou!')
print(f'EU pensei em {computador} e você digitou {usuario}!')
print('-=-' * 15)
