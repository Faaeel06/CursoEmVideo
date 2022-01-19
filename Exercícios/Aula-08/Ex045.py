# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice, shuffle
from time import sleep
opcao = ['Pedra', 'Papel', 'Tesoura']
shuffle(opcao)
computador = choice(opcao)
resultado = ''
print(f'{"=" * 20:>}', 'JOGO DE JOKENPÔ', f'{"=" * 20:>}')
print('Vamos começar o jogo...')
sleep(0.5)
print('Estou pensando minha opção...')
sleep(0.5)
print('Escolhi!!')
sleep(0.5)
print('Agora é sua vez.')
jogador = str(input('Digite sua opção: ')).title()
print(f'JO...')
sleep(0.25)
print(f'KEN...')
sleep(0.5)
print(f'PÔ!!!!')
if computador == 'Pedra' and jogador == 'Pedra':
    resultado = 'Poxa, empatamos!'
elif computador == 'Pedra' and jogador == 'Tesoura':
    resultado = 'Oba eu ganhei!! foi bom jogar com você humano!'
elif computador == 'Pedra' and jogador == 'Papel':
    resultado = 'Uau, muito bom! Você venceu!!'
elif computador == 'Tesoura' and jogador == 'Tesoura':
    resultado = 'Poxa, empatamos!'
elif computador == 'Tesoura' and jogador == 'Papel':
    resultado = 'Oba eu ganhei!! foi bom jogar com você humano!'
elif computador == 'Tesoura' and jogador == 'Pedra':
    resultado = 'Uau, muito bom! Você venceu!!'
elif computador == 'Papel' and jogador == 'Papel':
    resultado = 'Poxa, empatamos!'
elif computador == 'Papel' and jogador == 'Pedra':
    resultado = 'Oba eu ganhei!! foi bom jogar com você humano!'
elif computador == 'Papel' and jogador == 'Tesoura':
    resultado = 'Uau, muito bom! Você venceu!!'

print(f'{resultado}\n'
      f'Eu joguei {computador} e você jogou {jogador}')
