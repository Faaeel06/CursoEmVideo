# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time
count = 0
print('-=-' * 15)
print('=' * 5, 'Vamos jogar um jogo?', '=' * 5)
time.sleep(0.5)
print('Vou pensar em um número, tente advinhar')
time.sleep(0.5)
print('Pensando...')
time.sleep(1)
computador = random.randint(0, 11)
usuario = int(input('Digite sua opção entre 1 e 10: '))
while computador != usuario:
    if usuario != computador:
        count += 1
        print('Que pena! Você errou!')
        usuario = int(input('Digite sua opção entre 1 e 5: '))


print(f'EU pensei em {computador} e você digitou {usuario}! foram necessárias {count} tentativas')
print('-=-' * 15)
